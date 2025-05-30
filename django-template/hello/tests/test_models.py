import pytest
from django.contrib.auth.models import User
from hello.models import Libro, Resena

@pytest.mark.django_db
def test_crear_libro():
    """Verifica que se puede crear un libro y sus atributos son correctos."""
    libro = Libro.objects.create(
        titulo="Cien Años de Soledad",
        autor="Gabriel García Márquez",
        isbn="1234567890",
        descripcion="Novela famosa",
        anio_publicacion=1967,
        genero="Realismo mágico"
    )
    assert libro.titulo == "Cien Años de Soledad"
    assert libro.autor == "Gabriel García Márquez"
    assert libro.isbn == "1234567890"

@pytest.mark.django_db
def test_promedio_sin_resenas():
    """Verifica que el promedio de calificación es 0.0 si no hay reseñas."""
    libro = Libro.objects.create(
        titulo="Libro sin reseñas",
        autor="Autor",
        isbn="1111111111",
        descripcion="Sin reseñas",
        anio_publicacion=2000,
        genero="Ficción"
    )
    assert libro.obtener_promedio_calificacion() == 0.0

@pytest.mark.django_db
def test_promedio_con_resenas():
    """Verifica que el promedio de calificación es correcto con varias reseñas."""
    user = User.objects.create_user(username="testuser")
    libro = Libro.objects.create(
        titulo="Libro con reseñas",
        autor="Autor",
        isbn="2222222222",
        descripcion="Con reseñas",
        anio_publicacion=2001,
        genero="Ficción"
    )
    Resena.objects.create(libro=libro, usuario=user, comentario="Buena", calificacion=4)
    Resena.objects.create(libro=libro, usuario=user, comentario="Excelente", calificacion=5)
    promedio = libro.obtener_promedio_calificacion()
    assert promedio == 4.5

@pytest.mark.django_db
def test_libro_str():
    """Verifica que la representación en texto del libro es la esperada."""
    libro = Libro.objects.create(
        titulo="El Principito",
        autor="Antoine de Saint-Exupéry",
        isbn="3333333333",
        descripcion="Clásico",
        anio_publicacion=1943,
        genero="Fábula"
    )
    assert str(libro) == "El Principito - Antoine de Saint-Exupéry"


@pytest.mark.django_db
def test_crear_resena():
    """Verifica que se puede crear una reseña y sus atributos son correctos."""
    user = User.objects.create_user(username="resenador")
    libro = Libro.objects.create(
        titulo="Libro para reseña",
        autor="Autor",
        isbn="4444444444",
        descripcion="Libro de prueba",
        anio_publicacion=2020,
        genero="Drama"
    )
    resena = Resena.objects.create(
        libro=libro,
        usuario=user,
        comentario="Muy interesante",
        calificacion=5
    )
    assert resena.libro == libro
    assert resena.usuario == user
    assert resena.comentario == "Muy interesante"
    assert resena.calificacion == 5