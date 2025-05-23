from django import forms
from django.contrib.auth.models import User
from hello.models import LogMessage, Resena, Libro


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)

class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', max_length=150)
    email = forms.EmailField(label='Correo')

    class Meta:
        model = User
        fields = ['first_name', 'email']

class RegistroUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(label='Name', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']

class ResenaForm(forms.ModelForm):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), label="Libro", required=True)
    calificacion = forms.IntegerField(min_value=1, max_value=5, label="Calificación", widget=forms.HiddenInput())
    comentario = forms.CharField(widget=forms.Textarea, min_length=20, label="Comentario")

    class Meta:
        model = Resena
        fields = ['libro', 'comentario', 'calificacion']

class EditarResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['comentario']  