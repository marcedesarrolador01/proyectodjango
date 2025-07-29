# Documentación del Módulo de Modelos (`models.py`)

Este archivo contiene la definición de los modelos principales del proyecto del blog de autos. Estos modelos representan las entidades de datos que se almacenan y gestionan en la base de datos.

---

## Tabla de Contenidos

* [Categoria](#categoria)
* [Post](#post)
* [Comentario](#comentario)
* [Like](#like)
* [PerfilUsuario](#perfilusuario)
* [Imagen](#imagen)

---

## Categoria

Representa una categoría para agrupar los posts o imágenes.

**Campos:**

* `nombre`: Nombre de la categoría (texto, único).
* `slug`: Versión amigable para URL, generado automáticamente a partir del nombre.

**Meta:**

* `verbose_name_plural`: Cambia el nombre en plural a "Categorías".

**Métodos personalizados:**

* `save`: Genera el `slug` si no está definido.
* `__str__`: Retorna el nombre de la categoría.

---

## Post

Modelo principal del blog. Representa una publicación.

**Campos:**

* `titulo`: Título del post.
* `slug`: Slug amigable, generado desde el título.
* `contenido`: Cuerpo del post.
* `imagen`: Imagen del post.
* `autor`: Relación con el usuario autor del post.
* `categoria`: Categoría a la que pertenece.
* `fecha_creacion`: Fecha de creación.
* `fecha_actualizacion`: Fecha de última modificación.

**Meta:**

* `ordering`: Ordena por fecha de creación descendente.

**Métodos personalizados:**

* `save`: Genera el `slug` si no está definido.
* `total_likes`: Devuelve la cantidad de likes.
* `total_comentarios`: Devuelve la cantidad de comentarios.
* `__str__`: Retorna el título del post.

---

## Comentario

Modelo que representa un comentario hecho por un usuario sobre un post.

**Campos:**

* `post`: Post asociado.
* `usuario`: Usuario que hizo el comentario.
* `contenido`: Texto del comentario.
* `fecha_creacion`: Fecha en que se hizo el comentario.

**Meta:**

* `ordering`: Ordena los comentarios cronológicamente.

**Métodos personalizados:**

* `__str__`: Retorna una cadena indicando el usuario y el post comentado.

---

## Like

Modelo para registrar likes de usuarios en los posts.

**Campos:**

* `post`: Post que recibe el like.
* `usuario`: Usuario que da el like.

**Meta:**

* `unique_together`: Restringe para que un usuario no pueda dar más de un like al mismo post.

**Métodos personalizados:**

* `__str__`: Describe qué usuario dio like a qué post.

---

## PerfilUsuario

Modelo que extiende al usuario para controlar permisos adicionales, como la capacidad de publicar.

**Campos:**

* `user`: Usuario relacionado.
* `puede_publicar`: Booleano que indica si puede crear posts.

**Métodos personalizados:**

* `__str__`: Retorna el nombre de usuario.

---

## Imagen

Modelo para almacenar imágenes de una galería asociadas a una categoría.

**Campos:**

* `titulo`: Título de la imagen.
* `descripcion`: Texto descriptivo (opcional).
* `imagen`: Archivo de imagen.
* `categoria`: Categoría asociada.
* `fecha_creacion`: Fecha en la que se sube la imagen.

**Meta:**

* `ordering`: Ordena las imágenes más recientes primero.

**Métodos personalizados:**

* `__str__`: Devuelve el título de la imagen.

---

> Esta documentación es parte de la documentación técnica del proyecto "Blog de Autos" y está pensada para desarrolladores que trabajen en el mantenimiento o extensión del sistema.
