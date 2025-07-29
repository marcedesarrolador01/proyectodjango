# Documentación de Formularios (forms.py)

Este archivo contiene la definición de varios formularios utilizados en la aplicación del blog. Los formularios están basados en clases de Django y sirven para interactuar con modelos o para recibir datos personalizados del usuario.

---

## 1. ComentarioForm

**Ubicación**: `blog/forms.py`

Formulario basado en el modelo `Comentario`, utilizado para permitir que los usuarios escriban comentarios en las publicaciones.

```python
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario...'
            }),
        }
```

### Campos:

* `contenido`: Texto del comentario, con un widget personalizado (`Textarea`) para mejorar la experiencia de usuario.

### Uso:

Usado en la vista de detalle de un post para permitir agregar comentarios.

---

## 2. RegistroForm

Formulario personalizado para el registro de nuevos usuarios, extendiendo `UserCreationForm` de Django.

```python
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

### Campos:

* `username`: Nombre de usuario.
* `email`: Correo electrónico (campo adicional requerido).
* `password1` y `password2`: Contraseña y su confirmación.

### Uso:

Usado en el formulario de registro de nuevos usuarios.

---

## 3. PostForm

Formulario basado en el modelo `Post`, usado para crear o editar publicaciones en el blog.

```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
```

### Campos:

* `titulo`: Título del post.
* `contenido`: Texto del post.
* `imagen`: Imagen destacada.
* `categoria`: Categoría a la que pertenece el post.

### Uso:

Usado en el panel de administración de usuarios para crear/editar posts.

---

## 4. ContactoForm

Formulario simple (no basado en modelo) para que los usuarios puedan enviar consultas o mensajes de contacto.

```python
class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')
```

### Campos:

* `nombre`: Nombre del remitente.
* `email`: Correo electrónico del remitente.
* `mensaje`: Texto del mensaje enviado.

### Uso:

Se puede utilizar en una sección de contacto del sitio web para que los visitantes se comuniquen con los administradores.

---

## Consideraciones Generales

* Todos los formularios usan widgets de `Bootstrap` para mejorar el diseño visual.
* Los formularios basados en modelo (`ModelForm`) están vinculados directamente con los modelos definidos en `models.py`, lo que permite crear y validar datos automáticamente.
* Se recomienda usar `form.is_valid()` en las vistas para validar los formularios antes de guardar los datos.

---

## Archivos relacionados

* `models.py`: Contiene los modelos a los que están ligados algunos de estos formularios.
* `views.py`: Contiene las vistas que utilizan estos formularios.
* `templates/`: Carpeta que contiene los formularios renderizados en HTML.
