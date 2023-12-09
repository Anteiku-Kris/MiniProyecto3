from django.db import models

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

    def __str__(self):
        return f'Reseña de {self.producto.name}'