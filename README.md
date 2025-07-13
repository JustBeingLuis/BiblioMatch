# BiblioMatch UIS

BiblioMatch UIS es una plataforma web desarrollada con Django que permite a estudiantes y usuarios gestionar, buscar y reseñar libros en una biblioteca digital académica. El sistema está diseñado para facilitar el acceso a recursos bibliográficos, fomentar la interacción mediante reseñas y calificaciones, y ofrecer una experiencia moderna y segura de gestión de usuarios.

## Características principales

- **Autenticación de usuarios**: Registro, inicio de sesión tradicional y autenticación mediante Google OAuth2.
- **Gestión de libros**: Alta, visualización y búsqueda avanzada de libros por título, autor o descripción.
- **Historial de búsqueda**: Cada usuario puede consultar su historial de términos buscados.
- **Sistema de reseñas**: Los usuarios pueden crear, editar y eliminar reseñas de libros, así como calificar con estrellas.
- **Perfil de usuario**: Visualización y edición de datos personales.
- **Panel de administración**: Gestión de libros y reseñas desde el admin de Django.
- **Carga de portadas**: Soporte para imágenes de portada de libros.
- **Frontend moderno**: Interfaz responsiva y atractiva, con modales y efectos visuales.

## Estructura del proyecto

```
django-template/
├── .gitignore
├── manage.py
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements.txt
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── hello/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   └── hello/
│   ├── templates/
│   │   └── hello/
│   └── tests/
├── media/
│   └── portadas/
└── web_django/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Instalación y configuración

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/tu_usuario/bibliomatch-uis.git
   cd bibliomatch-uis/django-template
   ```

2. **Crea y activa un entorno virtual:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno para Google OAuth2 (opcional):**
   - Crea un archivo `google_oauth.txt` en la raíz del proyecto con el siguiente contenido:
     ```
     CLIENT_ID=tu_client_id_google
     CLIENT_SECRET=tu_client_secret_google
     ```

5. **Realiza las migraciones y crea un superusuario:**
   ```sh
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor de desarrollo:**
   ```sh
   python manage.py runserver
   ```

7. **Accede a la aplicación:**
   - Navega a [http://localhost:8000/](http://localhost:8000/) para usar la plataforma.
   - El panel de administración está en [http://localhost:8000/admin/](http://localhost:8000/admin/).

## Pruebas

El proyecto incluye pruebas unitarias para modelos y vistas. Puedes ejecutarlas con:

```sh
python manage.py test
```
o usando pytest si lo prefieres:

```sh
pytest
```

## Tecnologías utilizadas

- **Backend:** Django 5.x, Python 3.11+
- **Frontend:** HTML5, CSS3, JavaScript (vanilla)
- **Autenticación social:** [python-social-auth](https://python-social-auth.readthedocs.io/)
- **Base de datos:** SQLite (por defecto, fácilmente adaptable a otros motores)
- **Testing:** Django TestCase, Pytest


## Créditos

Desarrollado por Luis Toscano-Palomino para la Universidad Industrial de Santander (UIS).

---

¡Contribuciones y sugerencias son bienvenidas!
