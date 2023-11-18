from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "Core"

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(), name='login'),
]
