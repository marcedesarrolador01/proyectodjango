# whatsapp_bot/urls.py
from django.urls import path
from .views import webhook

urlpatterns = [
    path('webhook/', webhook, name='whatsapp_webhook'),
]
