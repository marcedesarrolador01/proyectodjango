# 📂 views.py – Vistas del proyecto AutoBlog

Este archivo contiene las vistas que gestionan la lógica principal del blog. Se divide en secciones como inicio, noticias, autenticación, manejo de posts, likes, comentarios, galería y contacto. A continuación, se documenta cada función por sección.

---

## 🏠 Home

### `home(request)`
- Muestra los últimos 6 posts publicados y todas las categorías.
- Vista principal (landing) del sitio.

---

## 📰 Noticias

### `noticias(request)`
- Muestra los posts con filtros por búsqueda (`q`), categoría y orden (por likes o comentarios).
- Implementa paginación para mostrar 9 posts por página.

---

## 📝 Detalle del post y comentarios

### `detalle_post(request, slug)`
- Muestra un post individual con sus comentarios.
- Permite a usuarios autenticados dejar un comentario.
- Verifica si el usuario ya dio like al post.

---

## ❤️ Likes

### `dar_like(request, post_id)`
- Agrega un like al post por parte del usuario autenticado.

### `quitar_like(request, post_id)`
- Quita el like dado por el usuario autenticado al post.

---

## 🔐 Autenticación

### `registro(request)`
- Registra un nuevo usuario mediante `RegistroForm`.
- Redirecciona al login si el registro fue exitoso.

### `login_view(request)`
- Vista de login utilizando el `AuthenticationForm`.
- Redirecciona a home si las credenciales son válidas.

### `logout_view(request)`
- Cierra sesión del usuario.
- Muestra un mensaje de éxito al salir.

### `sin_permiso(request)`
- Página de error para accesos no autorizados.

---

## ✍️ Crear, editar y eliminar posts

### `crear_post(request)`
- Permite a usuarios con permiso publicar nuevos posts.
- Usa `PostForm` y soporta archivos multimedia.

### `editar_post(request, slug)`
- Permite editar un post si es el autor o es superusuario.
- Valida permisos y redirecciona con mensajes de estado.

### `eliminar_post(request, slug)`
- Elimina un post tras confirmación y valida permisos.
- Redirige al home tras borrar.

---

## 🖼️ Galería

### `galeria(request)`
- Muestra imágenes filtradas por categoría o búsqueda.
- Implementa paginación de 9 imágenes por página.

---

## 📬 Contacto

### `contacto(request)`
- Muestra el formulario de contacto.
- Valida y guarda los datos del formulario.
- Muestra un mensaje de confirmación tras enviar.

---

## 👥 Nosotros

### `nosotros(request)`
- Vista estática que muestra información sobre el equipo o el blog.

---

## 📌 Notas generales

- Todas las vistas que requieren autenticación usan `@login_required`.
- Se usan `messages` para brindar feedback al usuario.
- La paginación se gestiona con `Paginator` de Django.
- Las búsquedas y filtros se implementan usando `Q` de Django ORM.

---

## 📎 Formularios usados

- `ComentarioForm`
- `RegistroForm`
- `PostForm`
- `ContactoForm`

---

## 📦 Modelos usados

- `Post`
- `Categoria`
- `Like`
- `Imagen`

---
