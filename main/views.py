import asyncio
import os
import json
import random
import string
import httpx
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TransmittedURL

# Функция для генерации короткого идентификатора
def generate_short_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            long_url = data.get('url')
        except json.JSONDecodeError:
            long_url = request.POST.get('url')

        if not long_url:
            return JsonResponse({'error': 'URL is required'}, status=400)

        # Проверяем, есть ли уже такой URL
        if TransmittedURL.objects.filter(long_url=long_url).exists():
            existing_entry = TransmittedURL.objects.get(long_url=long_url)
            return JsonResponse({'short_url': f'http://127.0.0.1:8000/{existing_entry.short_id}'}, status=200)

        short_id = generate_short_id()
        TransmittedURL.objects.create(long_url=long_url, short_id=short_id)
        return JsonResponse({'short_url': f'http://127.0.0.1:8000/{short_id}'}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


def redirect_to_original(request, short_id):
    url_entry = get_object_or_404(TransmittedURL, short_id=short_id)
    print(f"Редиректим на: {url_entry.long_url}")

    # Используем 307 Redirect
    response = HttpResponseRedirect(url_entry.long_url)
    response.status_code = 307
    return response
