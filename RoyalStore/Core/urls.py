from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import OtraVista
app_name = "Core"

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.productosvistas, name="productos"),
    path('agregar-productos/', views.agregarproducto, name="agregar-productos"),
    path('editar-productos/', views.editarproducto, name='editar-productos'),
    path('eliminar-productos/', views.eliminarproducto, name='eliminar-productos'),
    path('producto/<int:producto_id>/', views.detallesproductos, name='producto'),
    path('registro/', views.registro, name='registro'),
    path('contacts/', views.contacts, name="contacts"),
    path('login/', LoginView.as_view(), name='login'),
    path('otra-vista/<str:username>/', OtraVista.as_view(), name='otra_vista'),

]
