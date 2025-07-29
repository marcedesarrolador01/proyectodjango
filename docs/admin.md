# Documentación Técnica: admin.py

## Descripción General

El archivo `admin.py` del módulo `blog` contiene la configuración del panel de administración de Django para los modelos principales de la aplicación: `Categoria`, `Post`, `Comentario`, `Like`, `Imagen` y `PerfilUsuario`. A través de esta configuración, se definen aspectos como los campos visibles, opciones de filtrado, campos de búsqueda y configuraciones de solo lectura en la interfaz de administrador.

---

## Registro de Modelos en el Admin

### CategoriaAdmin

* **Modelo registrado:** `Categoria`
* **Decorador:** `@admin.register(Categoria)`
* **Opciones configuradas:**

  * `prepopulated_fields`: Rellena automáticamente el campo `slug` a partir de `nombre`.
  * `list_display`: Muestra `nombre` en la lista del admin.

### PostAdmin

* **Modelo registrado:** `Post`
* **Decorador:** `@admin.register(Post)`
* **Opciones configuradas:**

  * `prepopulated_fields`: Rellena `slug` a partir de `titulo`.
  * `list_display`: Campos visibles: `titulo`, `autor`, `categoria`, `fecha_creacion`.
  * `search_fields`: Permite búsqueda por `titulo` y `contenido`.
  * `list_filter`: Filtrado por `categoria` y `fecha_creacion`.
  * `readonly_fields`: Campos no editables: `fecha_creacion`, `fecha_actualizacion`.

### ComentarioAdmin

* **Modelo registrado:** `Comentario`
* **Decorador:** `@admin.register(Comentario)`
* **Opciones configuradas:**

  * `list_display`: Muestra `post`, `usuario` y `fecha_creacion`.

### LikeAdmin

* **Modelo registrado:** `Like`
* **Decorador:** `@admin.register(Like)`
* **Opciones configuradas:**

  * `list_display`: Muestra `post` y `usuario`.

### PerfilUsuarioAdmin

* **Modelo registrado:** `PerfilUsuario`
* **Decorador:** `@admin.register(PerfilUsuario)`
* **Opciones configuradas:**

  * `list_display`: Muestra `user` y `puede_publicar`.
  * `list_editable`: Permite editar `puede_publicar` directamente desde la vista de lista.

### ImagenAdmin

* **Modelo registrado:** `Imagen`
* **Decorador:** `@admin.register(Imagen)`
* **Opciones configuradas:**

  * `list_display`: Muestra `titulo`, `categoria` y `fecha_creacion`.
  * `list_filter`: Filtrado por `categoria` y `fecha_creacion`.
  * `search_fields`: Permite búsqueda por `titulo` y `descripcion`.

---

## Objetivo

Esta configuración personalizada permite que los administradores del sitio gestionen eficientemente los diferentes modelos a través del panel de administración de Django, mejorando la usabilidad y el control de los datos.

---

## Buenas Prácticas Aplicadas

* Uso de `@admin.register` para un código más limpio.
* Definición de `prepopulated_fields` para mejorar la creación de slugs.
* Uso de `list_display`, `list_filter`, `search_fields` y `readonly_fields` para optimizar la experiencia en el admin.

---

