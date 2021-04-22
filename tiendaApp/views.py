from django.shortcuts import render , HttpResponse

from tiendaApp.models import Producto, CategoriaProducto
# importar los servicios desde la app servicioApp

# Create your views here.

def tienda(request):
    productos=Producto.objects.all()
    categoriasPro = CategoriaProducto.objects.all()
    return render (request,'tiendaApp/tienda.html',{'productos':productos, 'categoriasPro':categoriasPro})

def tiendaPro(request,categoria_id):
    categoria= CategoriaProducto.objects.get(id=categoria_id)
    productos=Producto.objects.filter(categorias=categoria)
    return render(request,'tiendaApp/tiendaPro.html',{'categoria':categoria, 'productos':productos})
    
    