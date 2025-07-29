# BiblioMatch UIS

BiblioMatch UIS is a web platform developed with Django that allows students and users to manage, search for, and review books in an academic digital library. The system is designed to facilitate access to bibliographic resources, encourage interaction through reviews and ratings, and offer a modern and secure user management experience.

## Key Features

- **User Authentication:** Registration, traditional login, and authentication via Google OAuth2.
- **Book Management:** Create, view, and perform advanced search of books by title, author, or description.
- **Search History:** Each user can view their history of searched terms.
- **Review System:** Users can create, edit, and delete book reviews, as well as rate books with stars.
- **User Profile:** View and edit personal information.
- **Admin Panel:** Manage books and reviews through Django admin.
- **Cover Uploads:** Support for book cover images.
- **Modern Frontend:** Responsive and attractive interface with modals and visual effects.

## Project Structure

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

## Installation and Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your_username/bibliomatch-uis.git
   cd bibliomatch-uis/django-template


2. **Create and activate a virtual environment::**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables for Google OAuth2 (optional)**
   - Crea un archivo `google_oauth.txt` en la raíz del proyecto con el siguiente contenido:
     ```
     CLIENT_ID=tu_client_id_google
     CLIENT_SECRET=tu_client_secret_google
     ```

5. **Apply migrations and create a superuser:**
   ```sh
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the application:**
   - Navega a [http://localhost:8000/](http://localhost:8000/) para usar la plataforma.
   - El panel de administración está en [http://localhost:8000/admin/](http://localhost:8000/admin/).

## Testing

The project includes unit tests for models and views. You can run them with:

```sh
python manage.py test
```
or using pytest:

```sh
pytest
```

## 🛠️ Technologies Used

- **Backend:** Django 5.x, Python 3.11+
- **Frontend:** HTML5, CSS3, JavaScript (vanilla)
- **Social Authentication:** [python-social-auth](https://python-social-auth.readthedocs.io/)
- **Database:** SQLite (by default, easily adaptable to other engines)
- **Testing:** Django TestCase, Pytest

## 👨‍🎓 Credits

Developed by Luis Toscano-Palomino for the Industrial University of Santander (UIS).
