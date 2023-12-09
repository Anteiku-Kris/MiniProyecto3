from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request, "products.html")

def contacts(request):
    return render(request, "contacts.html")

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="Core:home")
        data["form"] = formulario
    return render(request, "registration/registro.html", data)

class OtraVista(View):
    def get(self, request, *args, **kwargs):
        # Lógica para la vista
        return render(request, 'registration/perfil.html', {'username': kwargs['username']})
