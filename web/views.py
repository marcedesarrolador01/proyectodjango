from django.shortcuts import render

def home(request):
    return render(request, 'web/home.html')

def contacto(request):
    return render(request, 'web/contacto.html')

def galeria(request):
    return render(request, 'web/galeria.html')

def noticias(request):
    return render(request, 'web/noticias.html')

def registro(request):
    return render(request, 'web/registro.html')

def login_view(request):
    return render(request, 'web/login.html')
