from django.urls import path
from .views import ShortenURLView, RedirectView

urlpatterns = [
    path('', ShortenURLView.as_view(), name='shorten_url'),
    path('<str:short_id>/', RedirectView.as_view(), name='redirect'),
]