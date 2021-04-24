from django.shortcuts import render

# importar la clase carro
from .carro import Carro
# importar los productos
from tiendaApp.models import Producto
# hacer redirecciones para que refleje los cambios del carro
from django.shortcuts import redirect

# Create your views here.

# vista agregar producto
def agregar_producto(request, producto_id):
    # crear carro
    carro= Carro(request)
    # obtener el producto
    producto =Producto.objects.get(id= producto_id)
    # agregar el producto al carro
    carro.agregar(producto=producto)
    # redireccionar a la tienda
    return redirect('tienda')

# vista eliminar producto
def eliminar_producto(request, producto_id):
    # crear carro
    carro= Carro(request)
    # obtener el producto
    producto =Producto.objects.get(id= producto_id)
    # eliminar el producto al carro
    carro.eliminar(producto=producto)
    # redireccionar a la tienda
    return redirect('tienda')

# vista restar producto
def restar_producto(request, producto_id):
    # crear carro
    carro= Carro(request)
    # obtener el producto
    producto =Producto.objects.get(id= producto_id)
    # agregar el producto al carro
    carro.restar_producto(producto=producto)
    # redireccionar a la tienda
    return redirect('tienda')

# vista limpiar el carro
def limpiar_carro(request, producto_id):
    # crear carro
    carro= Carro(request)
    # limpiar el carro
    carro.limpiar_carro()
    # redireccionar a la tienda
    return redirect('tienda')
