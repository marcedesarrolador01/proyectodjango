📄 Documentación Técnica – Vistas (blog/views.py)
📁 Módulo: blog.views
Este módulo contiene las vistas principales de la aplicación. Abarca funcionalidades como la visualización de publicaciones, detalles de post, sistema de comentarios y likes, autenticación de usuarios, y control de permisos de publicación.

📌 Índice de Vistas
home

detalle_post

dar_like

quitar_like

contacto

galeria

noticias

registro

login_view

logout_view

sin_permiso

crear_post

🔍 home(request)
Descripción
Vista principal del sitio. Muestra el listado de posts con capacidad de búsqueda, filtrado por categoría y ordenamiento por número de comentarios o likes.

Parámetros
request: objeto HttpRequest, puede contener parámetros GET:

q: cadena de búsqueda por título o autor.

categoria: slug de la categoría para filtrar.

orden: puede ser "comentarios" o "likes".

Contexto devuelto
posts: queryset filtrado de publicaciones.

categorias: lista de categorías disponibles.

🔍 detalle_post(request, slug)
Descripción
Vista de detalle de un post. Muestra el contenido completo, los comentarios existentes y el formulario para agregar uno nuevo si el usuario está autenticado. También verifica si el usuario ya dio like.

Parámetros
request: objeto HttpRequest.

slug: identificador único del post.

Funcionalidad adicional
Maneja el formulario de comentarios.

Verifica autenticación para comentar.

Devuelve indicador si el usuario ya dio like.

🔍 dar_like(request, post_id)
Descripción
Permite a un usuario autenticado darle like a una publicación.

Parámetros
post_id: ID numérico del post.

Requiere
Usuario autenticado (@login_required)

🔍 quitar_like(request, post_id)
Descripción
Permite a un usuario quitar su like de una publicación.

Parámetros
post_id: ID numérico del post.

Requiere
Usuario autenticado (@login_required)

🔍 contacto(request)
Descripción
Vista estática que muestra información de contacto.

🔍 galeria(request)
Descripción
Vista estática que muestra una galería de imágenes.

🔍 noticias(request)
Descripción
Vista estática que muestra una sección de noticias.

🔍 registro(request)
Descripción
Vista para el registro de nuevos usuarios. Utiliza el formulario RegistroForm.

Funcionalidad
Si el formulario es válido, guarda el usuario y redirige a la página de login.

Muestra mensajes de éxito o error con messages.

🔍 login_view(request)
Descripción
Vista para iniciar sesión. Utiliza el formulario AuthenticationForm.

Funcionalidad
Autentica al usuario.

Redirige a la página principal (home) tras inicio exitoso.

Muestra errores si las credenciales son incorrectas.

🔍 logout_view(request)
Descripción
Cierra la sesión del usuario actual.

Funcionalidad
Muestra mensaje de éxito al cerrar sesión.

Redirige a home.

🔍 sin_permiso(request)
Descripción
Muestra una página personalizada cuando un usuario no tiene permisos para realizar una acción (por ejemplo, crear un post).

🔍 crear_post(request)
Descripción
Permite a un usuario con permisos especiales (PerfilUsuario.puede_publicar = True) crear una nueva publicación.

Funcionalidad
Valida el permiso del perfil.

Procesa el formulario PostForm (incluye imagen).

Guarda el post asociado al usuario autenticado.

Requiere
Usuario autenticado (@login_required)

Permiso de publicación activo en el perfil del usuario.

📎 Notas adicionales
Se utiliza messages para mejorar la comunicación con el usuario.

Todas las vistas están integradas con plantillas (templates/) para renderizado dinámico.

El acceso a ciertas acciones está protegido por @login_required.

Los likes y comentarios se controlan por modelo y lógica simple en vistas.

