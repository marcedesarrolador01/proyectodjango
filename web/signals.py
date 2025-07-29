
from django.db.models.signals import post_save  # Señal que se dispara después de guardar un modelo
from django.contrib.auth.models import User      # Modelo de usuario de Django
from django.dispatch import receiver              # Decorador para registrar funciones como receptores de señales
from .models import PerfilUsuario                 # Modelo de perfil de usuario extendido

# Esta función se ejecuta automáticamente cuando se crea un nuevo usuario

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Crea un perfil asociado al nuevo usuario
        PerfilUsuario.objects.create(user=instance)

# Esta función se ejecuta cada vez que un usuario es guardado

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    # Guarda automáticamente el perfil relacionado con el usuario
    instance.perfilusuario.save()
