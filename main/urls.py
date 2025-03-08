from django.urls import path
from .views import async_func, shorten_url, redirect_to_original

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('<str:short_id>/', redirect_to_original, name='redirect'),
    path('async/<str:service_name>/', async_func, name='async_func'),
]