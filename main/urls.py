from django.urls import path
from .views import shorten_url, redirect_to_original

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('<str:short_id>/', redirect_to_original, name='redirect'),
]
