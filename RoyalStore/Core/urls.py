from django.urls import path
from . import views

app_name = "Core"

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('registro/', views.registro, name="registro"),
]
