from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TransmittedURL
import uuid
import httpx
from .models import TransmittedURL


@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if not long_url:
            return JsonResponse({'error': 'URL is required'}, status=400)
        short_id = str(uuid.uuid4())[:8]
        TransmittedURL.objects.create(long_url=long_url, short_id=short_id)
        return JsonResponse({'short_url': f'http://127.0.0.1:8080/{short_id}'}, status=201)
    return JsonResponse({'error': 'not allowed'}, status=405)


def redirect_to_original(request, short_id):
    try:
        url_entry = TransmittedURL.objects.get(short_id=short_id)
        return HttpResponseRedirect(url_entry.long_url, status=307)
    except TransmittedURL.DoesNotExist:
        return HttpResponseNotFound('Short URL not found')


async def async_func(request, service_name):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f'https://api.example.com/{service_name}')
            response.raise_for_status()
            return JsonResponse(response.json())
        except httpx.HTTPStatusError as e:
            return JsonResponse({'error': 'External service error'}, status=e.response.status_code)