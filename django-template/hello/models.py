from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    anio_publicacion = models.IntegerField()
    genero = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def obtener_promedio_calificacion(self):
        reseñas = self.resena_set.all()
        if reseñas.exists():
            return sum([r.calificacion for r in reseñas]) / reseñas.count()
        return 0.0

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class HistorialBusqueda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    termino = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username}: {self.termino} ({self.fecha})"
    

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.PositiveSmallIntegerField()  # 1 a 5
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.libro.titulo} ({self.calificacion} estrellas)"