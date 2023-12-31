from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Productos(models.Model):
    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
        ordering = ["name"]

    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, null=True, upload_to="productos")
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Resena(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    comentario = models.TextField()
    puntuacion = models.PositiveIntegerField(default=0)  # Campo para almacenar la puntuación

    def str(self):
        return f'Reseña de {self.producto.name}'

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True, default='default_profile_pic.jpg')
    bio = models.TextField(max_length=500, blank=True)
    favorites=models.ManyToManyField(Productos,blank=True)
    

    def str(self):
        return self.user.username


    