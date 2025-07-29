# Documentación Técnica: signals.py

Este archivo contiene la lógica de señales (`signals`) utilizada para extender el comportamiento del modelo de usuario (`User`) de Django automáticamente. En particular, se asegura que cada vez que se crea o guarda un usuario, su perfil asociado (`PerfilUsuario`) también se cree o guarde.

## Descripción de las señales

### Señal: `crear_perfil_usuario`

- **Propósito**: Crear automáticamente un perfil de usuario (`PerfilUsuario`) cuando se registra un nuevo usuario (`User`).
- **Decorador**: `@receiver(post_save, sender=User)`
- **Parámetros**:
  - `sender`: Modelo que envía la señal, en este caso `User`.
  - `instance`: Instancia del usuario que se ha creado.
  - `created`: Booleano que indica si la instancia se acaba de crear.
  - `**kwargs`: Argumentos adicionales.

```python
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)
```

### Señal: `guardar_perfil_usuario`

- **Propósito**: Guardar automáticamente el perfil asociado cuando se actualiza un usuario.
- **Decorador**: `@receiver(post_save, sender=User)`
- **Parámetros**:
  - `sender`: Modelo que envía la señal, en este caso `User`.
  - `instance`: Instancia del usuario que se ha guardado.
  - `**kwargs`: Argumentos adicionales.

```python
@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfilusuario.save()
```

## Importancia en el proyecto

Estas señales permiten mantener sincronizados los modelos `User` y `PerfilUsuario` sin requerir lógica explícita en las vistas o formularios. Es una técnica comúnmente usada para extender el modelo de usuario predeterminado de Django sin modificarlo directamente.

---

> Archivo relacionado: `models.py` (donde se define `PerfilUsuario`)
> Uso típico: Este archivo debe estar importado o conectado en `apps.py` dentro de `ready()` para que Django cargue las señales.