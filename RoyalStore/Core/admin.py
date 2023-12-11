from django.contrib import admin
from .models import Productos, Categoria, Resena, Contacto, UserProfile

admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(Resena)
admin.site.register(Contacto)
admin.site.register(UserProfile)
