from django.shortcuts import render , HttpResponse

from .models import Producto, CategoriaProducto
# importar los servicios desde la app servicioApp

# Create your views here.

def tienda(request):
    productos=Producto.objects.all()
    categoriasProducto = CategoriaProducto.objects.all()
    return render (request,'tiendaApp/tienda.html',{'productos':productos,'categoriasProducto':categoriasProducto})

def categoriaProducto(request, categoriaProducto_id):
    # en una variable recuperamos el id que tengo dentro de la clase categoria
    categoriaProducto = CategoriaProducto.objects.get(id=categoriaProducto_id)
    # filtramos los post en base a la categoria
    productos= Productos.objects.filter(categorias=categoriaProducto)
    return render (request,'TiendaApp/categoriaProducto.html',{'categoriaProducto':categoriaProducto,'productos':productos})