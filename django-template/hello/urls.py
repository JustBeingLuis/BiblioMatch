from django.urls import path
from hello import views
from hello.models import LogMessage
from hello import views

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("log/", views.log_message, name="log"),
    path('buscar/', views.buscar_libros, name='buscar_libros'),
    path('historial/', views.historial_busqueda, name='historial_busqueda'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_view, name='login'),
    path('resenas/crear/', views.crear_resena, name='crear_resena'),
    path('resenas/<int:libro_id>/', views.detalles_libro, name='detalles_libro'),
    path('libro/<int:libro_id>/modal/', views.detalles_libro_modal, name='detalles_libro_modal'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('mis-resenas/', views.mis_resenas, name='mis_resenas'),
    path('resena/editar/<int:resena_id>/', views.editar_resena, name='editar_resena'),
    path('resena/eliminar/<int:resena_id>/', views.eliminar_resena, name='eliminar_resena'),
]

