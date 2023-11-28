from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import OtraVista
app_name = "Core"

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('otra-vista/<str:username>/', OtraVista.as_view(), name='otra_vista'),

]
