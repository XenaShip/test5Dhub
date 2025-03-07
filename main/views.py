from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TransmittedURL
from .serializers import ShortURLSerializer

class ShortenURLView(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            short_url = serializer.save()
            print('OK. 201_CREATED')
            return Response(ShortURLSerializer(short_url, context={'request': request}).data, status=status.HTTP_201_CREATED)
        else:
            print('400_BAD_REQUEST')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectView(APIView):
    def get(self, request, short_id):
        short_url = get_object_or_404(TransmittedURL, short_id=short_id)
        return redirect(short_url.original_url)