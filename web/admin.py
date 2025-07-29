from django.contrib import admin
from .models import Categoria, Post, Comentario, Like, Imagen, PerfilUsuario

# Configuración del panel de administración para el modelo Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}
    list_display = ("nombre",)

# Configuración del panel de administración para el modelo Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    list_display = ("titulo", "autor", "categoria", "fecha_creacion")
    search_fields = ("titulo", "contenido")
    list_filter = ("categoria", "fecha_creacion")
    readonly_fields = ("fecha_creacion", "fecha_actualizacion")

# Configuración del panel de administración para el modelo Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("post", "usuario", "fecha_creacion")

# Configuración del panel de administración para el modelo Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post", "usuario")

# Configuración del panel de administración para el modelo PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("user", "puede_publicar")
    list_editable = ("puede_publicar",)

# Configuración del panel de administración para el modelo Imagen

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_creacion')
    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
