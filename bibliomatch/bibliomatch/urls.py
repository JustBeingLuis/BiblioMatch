from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # URLs de login, logout, signup
    path('', include('core.urls')),              # URLs principales de tu app
]
