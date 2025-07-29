
# 📁 `urls.py` – Rutas del proyecto Blog de Autos

Este archivo define las rutas (URLs) disponibles en la aplicación principal del blog. Cada ruta está asociada a una vista específica que maneja la lógica correspondiente. Utiliza `path()` del módulo `django.urls`.

---

## 🔗 Rutas definidas

| URL | Vista asociada | Nombre | Descripción |
|-----|----------------|--------|-------------|
| `'/'` | `views.home` | `home` | Página principal del blog, muestra los últimos posts. |
| `'noticias/'` | `views.noticias` | `noticias` | Página de noticias o artículos del blog. |
| `'post/<slug:slug>/'` | `views.detalle_post` | `detalle_post` | Muestra el contenido completo de un post individual. |
| `'like/<int:post_id>/'` | `views.dar_like` | `dar_like` | Permite dar "me gusta" a un post específico. |
| `'unlike/<int:post_id>/'` | `views.quitar_like` | `quitar_like` | Permite quitar un "me gusta" dado anteriormente. |
| `'contacto/'` | `views.contacto` | `contacto` | Formulario de contacto para enviar mensajes al equipo del blog. |
| `'nosotros/'` | `views.nosotros` | `nosotros` | Página de información sobre el blog y su equipo. |
| `'registro/'` | `views.registro` | `registro` | Formulario de registro de nuevos usuarios. |
| `'login/'` | `views.login_view` | `login` | Página de inicio de sesión. |
| `'logout/'` | `views.logout_view` | `logout` | Cierra la sesión del usuario actual. |
| `'crear-post/'` | `views.crear_post` | `crear_post` | Página para crear un nuevo post (requiere permisos). |
| `'post/<slug:slug>/editar/'` | `views.editar_post` | `editar_post` | Página para editar un post existente. |
| `'post/<slug:slug>/eliminar/'` | `views.eliminar_post` | `eliminar_post` | Página para eliminar un post. |
| `'galeria/'` | `views.galeria` | `galeria` | Página de galería de imágenes del blog. |

---

## 🧩 Observaciones

- Se hace uso de `slug` para identificar los posts, lo que mejora la legibilidad y SEO.
- Las rutas para dar/quitar like utilizan `post_id` (tipo `int`).
- Todas las vistas están importadas directamente desde `views.py`.
