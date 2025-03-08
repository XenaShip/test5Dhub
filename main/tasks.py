from celery import shared_task
from .models import TransmittedURL

@shared_task
def delete_old_urls():
    TransmittedURL.objects.filter(created_at__lt='2024-01-01').delete()
