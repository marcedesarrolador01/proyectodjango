from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Modelo para representar categorías de los posts

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def save(self, *args, **kwargs):
        # Generar automáticamente el slug si no está definido
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

# Modelo principal para representar publicaciones en el sitio

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='posts')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']  # Mostrar posts más recientes primero

    def save(self, *args, **kwargs):
        # Generar automáticamente el slug a partir del título si no existe
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def total_comentarios(self):
        return self.comentarios.count()

    def __str__(self):
        return self.titulo

# Modelo para almacenar comentarios de usuarios en los posts

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_creacion']  # Mostrar comentarios en orden cronológico

    def __str__(self):
        return f'Comentario de {self.usuario.username} en "{self.post.titulo}"'

# Modelo para registrar likes de usuarios a los posts

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('post', 'usuario')  # Evita que un usuario dé más de un like al mismo post

    def __str__(self):
        return f'{self.usuario.username} le dio like a "{self.post.titulo}"'

# Modelo de perfil extendido para controlar permisos adicionales del usuario

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puede_publicar = models.BooleanField(default=False)  # Permiso para crear posts

    def __str__(self):
        return self.user.username

# Modelo para imágenes de la galería
# Galería de imágenes asociadas a una categoría existente

class Imagen(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='galeria/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='imagenes')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']  # Más recientes primero

    def __str__(self):
        return self.titulo

