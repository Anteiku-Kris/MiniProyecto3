from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .forms import  AgregarproductosForm, CustomUserCreationForm, ResenaForm
from django.contrib.auth import authenticate, login
from .models import Productos, Categoria, Resena
from django.urls import reverse

def home(request):
    return render(request, "home.html")

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
    
def productosvistas(request): 
    categorias = Categoria.objects.all()
    # Un diccionario para almacenar las categorías y sus productos asociados
    categorias_con_productos = {}

    for categoria in categorias:
          # Filtrar productos por categoría
        productos = Productos.objects.filter(category=categoria)
        categorias_con_productos[categoria] = productos

    return render(request, 'products.html', {'categorias_con_productos': categorias_con_productos})


def agregarproducto(request):
    if request.method == "POST":
        form = AgregarproductosForm(request.POST, request.FILES)
        if form.is_valid():
            # Guarda el producto en la base de datos
            form.save()
            return redirect('Core:productos')
    else:
        form = AgregarproductosForm()

    categorias = Categoria.objects.all() 
    return render(request, "agregar-productos.html", {"form": form, "categorias": categorias})

def cargar_producto(producto_id):
    try:
        return Productos.objects.get(id=producto_id)
    except Productos.DoesNotExist:
        return None

def editarproducto(request):
    producto_id = None
    if request.method == 'POST':
         # Obtener el producto seleccionado
        producto_id = request.POST.get('product_select') 
        # Cargar el producto a editar
        producto = cargar_producto(producto_id)


        if producto is not None:
            form = AgregarproductosForm(request.POST, request.FILES, instance=producto)

            if form.is_valid():
                form.save() 
                return redirect('Core:productos')

    else:
        form = AgregarproductosForm(instance=None)

    productos = Productos.objects.all()
    categorias = Categoria.objects.all()



    context = {
        'form': form,
        'producto_id': producto_id,
        'productos': productos,
        'categorias': categorias,
    }

    return render(request, 'editar-productos.html', context)

def eliminarproducto(request):
    mensaje_error = None
    if request.method:
        producto_id = request.POST.get('producto_id')
        try:
            producto = Productos.objects.get(pk=producto_id)
            producto.delete()
            return redirect('Core:productos')
        except Productos.DoesNotExist:
            mensaje_error = "La categoria seleccionada no existe."
    productos = Productos.objects.all()
    return render(request, 'eliminar-productos.html', {"productos": productos})
    



def detallesproductos(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)
    resenas = Resena.objects.filter(producto=producto)

    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            puntuacion = request.POST['puntuacion']  # la puntuación del POST

            # Crea la nueva reseña con el comentario y la puntuación
            Resena.objects.create(producto=producto, comentario=comentario, puntuacion=puntuacion)

            # Redirige a la vista 'producto' con el parámetro producto_id
            url = reverse('Core:producto', args=[producto_id])
            return redirect(url)

    else:
        form = ResenaForm()

    context = {
        'producto': producto,
        'reseñas': resenas,
        'form': form,
    }
    
    return render(request, 'detalles-productos.html', context)


