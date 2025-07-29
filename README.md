
# AutoBlog - Plataforma de Publicaciones sobre Automóviles 🚗📰

AutoBlog es una aplicación web desarrollada con Django que permite crear, gestionar y visualizar publicaciones (noticias, artículos, galerías) relacionadas al mundo automotor. Los usuarios pueden registrarse, comentar, dar like, subir imágenes y mucho más.

---

## 📁 Estructura de Aplicación

### Modelos (`models.py`)
- **Categoria**: Clasificación de los posts e imágenes.
- **Post**: Publicación con título, contenido, imagen, autor, categoría, likes y comentarios.
- **Comentario**: Comentarios de usuarios asociados a un post.
- **Like**: Registro de "me gusta" de usuarios a los posts.
- **PerfilUsuario**: Extiende al usuario con permisos de publicación.
- **Imagen**: Imágenes para la galería, asociadas a categorías.

### Señales (`signals.py`)
- Crea automáticamente un perfil de usuario al registrarse.
- Guarda cambios en el perfil cuando se actualiza el usuario.

### Vistas (`views.py`)
- `home`: Página principal con últimos posts.
- `noticias`: Listado filtrable y ordenable de publicaciones.
- `detalle_post`: Muestra un post y sus comentarios.
- `dar_like`, `quitar_like`: Añadir o quitar likes.
- `registro`, `login_view`, `logout_view`: Gestión de usuarios.
- `crear_post`, `editar_post`, `eliminar_post`: ABM de publicaciones (requiere permisos).
- `galeria`: Galería de imágenes.
- `contacto`: Formulario de contacto.
- `nosotros`: Información institucional.

---

## 🔐 Autenticación y Permisos

- Solo usuarios registrados pueden comentar o dar likes.
- Solo usuarios con permiso (`puede_publicar=True`) pueden crear posts.
- El autor del post o un superusuario puede editar o eliminar publicaciones.

---

## 🎨 Funcionalidades del Frontend

- Bootstrap 5 + FontAwesome para UI moderna y responsiva.
- Búsqueda, filtros y paginación para noticias y galería.
- Mensajes informativos (Django messages) para feedback de acciones.

---

## 🖼️ Carga de Imágenes

- Post: Campo opcional de imagen principal.
- Galería: Imágenes cargadas con título, descripción y categoría.
- Archivos se almacenan en las rutas `posts/` y `galeria/`.

---

## 📌 Slugs automáticos

Los modelos `Post` y `Categoria` generan automáticamente slugs amigables para URLs a partir del título o nombre.

---

## 🧩 Formularios

- `ComentarioForm`: Agregar comentarios.
- `RegistroForm`: Registro personalizado.
- `PostForm`: Crear y editar publicaciones.
- `ContactoForm`: Formulario de contacto simple.

---

## 🔄 Señales

Configuradas para crear automáticamente un perfil extendido al crear un nuevo `User`, y para mantener sincronizado el perfil al actualizar el usuario.

---

## 📊 Visualización del Modelo de Datos con dbdiagram.io

Para facilitar la comprensión, mantenimiento y comunicación del esquema de base de datos del proyecto, se recomienda visualizar las tablas y sus relaciones en una herramienta especializada como [dbdiagram.io](https://dbdiagram.io).

Este proyecto cuenta con un modelo relacional bien definido, con relaciones claras entre usuarios, posts, categorías, comentarios, likes y galería de imágenes. Entender estas relaciones es clave para ampliar, optimizar o integrar nuevas funcionalidades.

Puedes acceder al diagrama interactivo y actualizado del modelo de datos aquí:

[👉 Ver Diagrama en dbdiagram.io](https://dbdiagram.io/d/68884f2acca18e685c2a98a7)

### ¿Por qué usar dbdiagram.io?

- **Visualización clara:** Permite entender de un vistazo las tablas, columnas, tipos y relaciones entre ellas.
- **Documentación viva:** Sirve como documentación técnica accesible para todo el equipo.
- **Facilita el onboarding:** Nuevos desarrolladores comprenden rápido el esquema sin leer todo el código.
- **Base para decisiones:** Ayuda a planificar cambios estructurales o integraciones con terceros.
- **Exportación:** Puedes exportar el esquema a SQL, PNG, PDF, etc.

---

## 🔚 Consideraciones finales

- Ideal para blogs automotores, revistas digitales o proyectos personales.
- Estructura profesional y mantenible.
- Fácil de extender con funciones como etiquetas, favoritos, suscripciones, etc.

---
