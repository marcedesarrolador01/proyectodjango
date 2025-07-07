
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('galeria/', views.galeria, name='galeria'),
    path('noticias/', views.noticias, name='noticias'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
]
