from django import forms
from .models import Productos, Categoria, Resena
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', "first_name", "last_name", "email", "password1", "password2")

class AgregarproductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('name', 'description', 'price', 'image', 'category')	

class CategoriaForm(forms.ModelForm):
     # Recupera las categorías desde la base de datos
    categorias = [(c.id, c.name) for c in Categoria.objects.all()] 
     # Opciones para el campo "categoria"
    categoria = forms.ChoiceField(choices=categorias, required=False) 
    name = forms.CharField()
    description = forms.CharField()

    class Meta:
        model = Categoria
        fields =('name','description','categoria', )


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

        
class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['comentario', 'puntuacion']