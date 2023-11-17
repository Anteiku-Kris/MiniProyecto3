from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request, "products.html")

def registro(request):
    return render(request, "registration/registro.html")
