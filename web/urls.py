from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticias/', views.noticias, name='noticias'),
    path('post/<slug:slug>/', views.detalle_post, name='detalle_post'),
    path('like/<int:post_id>/', views.dar_like, name='dar_like'),
    path('unlike/<int:post_id>/', views.quitar_like, name='quitar_like'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('post/<slug:slug>/editar/', views.editar_post, name='editar_post'),
    path('post/<slug:slug>/eliminar/', views.eliminar_post, name='eliminar_post'),
    path('galeria/', views.galeria, name='galeria'),
]
