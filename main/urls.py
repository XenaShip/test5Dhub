from django.urls import path
from .views import ShortenURLView, RedirectView, async_func

urlpatterns = [
    path('', ShortenURLView.as_view(), name='shorten_url'),
    path('<str:short_id>/', RedirectView.as_view(), name='redirect'),
    path('async/<str:service_name>/', async_func.as_view(), name='async_func'),
]