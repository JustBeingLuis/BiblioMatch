import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q, Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from hello.forms import LogMessageForm, RegistroUsuarioForm, ResenaForm, EditarPerfilForm, EditarResenaForm
from hello.models import LogMessage, Libro, HistorialBusqueda, Resena

# ==========================
# Vistas de Autenticación
# ==========================

def registro_usuario(request):
    """
    Permite a un nuevo usuario registrarse en el sistema.
    """
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            usuario.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, usuario)
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'hello/registro_usuario.html', {'form': form})

class CustomLoginView(LoginView):
    """
    Vista personalizada para el inicio de sesión usando LoginView de Django.
    """
    template_name = 'hello/login.html'

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'hello/login.html', {'form': form})

# ==========================
# Vistas Principales
# ==========================

class HomeListView(ListView):
    """
    Renderiza la página principal mostrando todos los mensajes.
    """
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    """
    Renderiza la página 'Acerca de'.
    """
    return render(request, "hello/about.html")

# ==========================
# Vistas de Mensajes
# ==========================

def log_message(request):
    """
    Permite crear un nuevo mensaje de log.
    """
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    return render(request, "hello/log_message.html", {"form": form})

# ==========================
# Vistas de Libros y Búsqueda
# ==========================

def buscar_libros(request):
    """
    Permite buscar libros por título, autor o descripción.
    Guarda el historial de búsqueda si el usuario está autenticado.
    """
    query = request.GET.get('q', '')
    if query:
        if request.user.is_authenticated:
            HistorialBusqueda.objects.create(usuario=request.user, termino=query)
        resultados = Libro.objects.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(descripcion__icontains=query)
        )
    else:
        resultados = Libro.objects.all()
    return render(request, 'hello/busqueda_libros.html', {
        'resultados': resultados,
        'query': query
    })

@login_required
def historial_busqueda(request):
    """
    Muestra el historial de búsqueda del usuario autenticado.
    """
    historial = HistorialBusqueda.objects.filter(usuario=request.user).order_by('-fecha')[:20]
    return render(request, 'hello/historial_busqueda.html', {'historial': historial})

@login_required
def detalles_libro(request, libro_id):
    """
    Muestra los detalles de un libro y sus reseñas.
    """
    libro = get_object_or_404(Libro, id=libro_id)
    resenas = Resena.objects.filter(libro=libro).order_by('-fecha')
    promedio = libro.obtener_promedio_calificacion()
    return render(request, 'hello/detalles_libro.html', {
        'libro': libro,
        'resenas': resenas,
        'promedio': promedio
    })

def detalles_libro_modal(request, libro_id):
    """
    Devuelve los detalles de un libro y sus reseñas para mostrar en un modal.
    """
    libro = get_object_or_404(Libro, pk=libro_id)
    resenas = Resena.objects.filter(libro=libro).select_related('usuario').order_by('-fecha')
    promedio = resenas.aggregate(Avg('calificacion'))['calificacion__avg'] or 0
    return render(request, 'hello/modal_detalles_libro.html', {
        'libro': libro,
        'resenas': resenas,
        'promedio': promedio,
    })

# ==========================
# Vistas de Reseñas
# ==========================

@login_required
def crear_resena(request):
    """
    Permite a un usuario autenticado crear una reseña para un libro.
    """
    mensaje_exito = None
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.usuario = request.user
            resena.save()
            mensaje_exito = "¡Reseña enviada con éxito!"
            form = ResenaForm()  # Limpia el formulario
    else:
        form = ResenaForm()
    return render(request, 'hello/crear_resena.html', {'form': form, 'mensaje_exito': mensaje_exito})

@login_required
def mis_resenas(request):
    resenas = Resena.objects.filter(usuario=request.user)
    return render(request, 'hello/mis_resenas.html', {'resenas': resenas})

@login_required
def editar_resena(request, resena_id):
    resena = get_object_or_404(Resena, id=resena_id, usuario=request.user)
    if request.method == 'POST':
        form = EditarResenaForm(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            return redirect('mis_resenas')
    else:
        form = EditarResenaForm(instance=resena)
    return render(request, 'hello/editar_resena.html', {'form': form, 'resena': resena})

@login_required
def eliminar_resena(request, resena_id):
    resena = get_object_or_404(Resena, id=resena_id, usuario=request.user)
    if request.method == 'POST':
        resena.delete()
        return redirect('mis_resenas')
    return render(request, 'hello/eliminar_resena.html', {'resena': resena})

# ==========================
# Vistas de perfil y edición de usuario
# ==========================

@login_required
def perfil_usuario(request):
    return render(request, 'hello/perfil_usuario.html', {'usuario': request.user})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil_usuario')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'hello/editar_perfil.html', {'form': form})