from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count, Q
from django.core.paginator import Paginator
from .models import Post, Categoria, Like, Imagen
from .forms import ComentarioForm, RegistroForm, PostForm, ContactoForm

# Home

def home(request):
    posts = Post.objects.order_by('-fecha_creacion')[:6]
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'categorias': categorias
    })

# Noticias

def noticias(request):
    query = request.GET.get('q')
    categoria_slug = request.GET.get('categoria')
    orden = request.GET.get('orden')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(Q(titulo__icontains=query) | Q(autor__username__icontains=query))
    if categoria_slug:
        posts = posts.filter(categoria__slug=categoria_slug)

    if orden == 'comentarios':
        posts = posts.annotate(num_comentarios=Count('comentarios')).order_by('-num_comentarios')
    elif orden == 'likes':
        posts = posts.annotate(num_likes=Count('likes')).order_by('-num_likes')
    else:
        posts = posts.order_by('-fecha_creacion')

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, 'noticias.html', {
        'page_obj': page_obj,
        'categorias': categorias
    })

# Detalle de post y comentarios

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comentarios = post.comentarios.all().order_by('fecha_creacion')
    nuevo_comentario = None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, "Debes iniciar sesión para comentar.")
            return redirect('login')

        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.usuario = request.user
            nuevo_comentario.save()
            messages.success(request, "Comentario agregado correctamente.")
            return redirect('detalle_post', slug=slug)
    else:
        form = ComentarioForm()

    ya_dio_like = request.user.is_authenticated and Like.objects.filter(post=post, usuario=request.user).exists()

    return render(request, 'detalle_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
        'nuevo_comentario': nuevo_comentario,
        'ya_dio_like': ya_dio_like,
    })

# Likes

@login_required
def dar_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(post=post, usuario=request.user)
    return redirect('detalle_post', slug=post.slug)

@login_required
def quitar_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(post=post, usuario=request.user).delete()
    return redirect('detalle_post', slug=post.slug)

# Autenticación

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora podés iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')

def sin_permiso(request):
    return render(request, 'web/sin_permiso.html')

# Crear / Editar / Eliminar Post

@login_required
def crear_post(request):
    perfil = request.user.perfilusuario
    if not perfil.puede_publicar:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalle_post', slug=post.slug)
    else:
        form = PostForm()

    return render(request, 'web/crear_post.html', {'form': form})

@login_required
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user != post.autor and not request.user.is_superuser:
        messages.error(request, "No tenés permiso para editar este post.")
        return redirect('detalle_post', slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado correctamente.")
            return redirect('detalle_post', slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'web/editar_post.html', {'form': form, 'post': post})

@login_required
def eliminar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user != post.autor and not request.user.is_superuser:
        messages.error(request, "No tenés permiso para eliminar este post.")
        return redirect('detalle_post', slug=slug)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post eliminado correctamente.")
        return redirect('home')

    return render(request, 'web/eliminar_post.html', {'post': post})

# Galería de imágenes

def galeria(request):
    query = request.GET.get('q')
    categoria_slug = request.GET.get('categoria')

    imagenes = Imagen.objects.all()

    if categoria_slug:
        imagenes = imagenes.filter(categoria__slug=categoria_slug)
    elif query:
        imagenes = imagenes.filter(titulo__icontains=query)

    paginator = Paginator(imagenes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, 'galeria.html', {
        'page_obj': page_obj,
        'imagenes': page_obj.object_list,
        'categorias': categorias,
        'categoria_activa': categoria_slug,
        'query': query,
    })

# Contactos

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Gracias por tu mensaje. Te responderemos pronto.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
 
#Nosotros
def nosotros(request):
    return render(request, 'web/nosotros.html')
