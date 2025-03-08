import os
from datetime import timedelta
from celery import shared_task, Celery
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from test.main.models import TransmittedURL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')
app = Celery('test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
