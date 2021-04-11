from django.shortcuts import render
from blogApp.models import Post, Categoria

# Create your views here.

def blog(request):
    # en una variable recuperamos todos los objetos que tengo dentro de la clase Servicio
    entradas= Post.objects.all()
    return render (request,'blogApp/blog.html',{'entradas':entradas})


def categoria(request, categoria_id):
    # en una variable recuperamos el id que tengo dentro de la clase categoria
    categoria = Categoria.objects.get(id=categoria_id)
    # filtramos los post en base a la categoria
    entradas= Post.objects.filter(categorias=categoria)
    return render (request,'blogApp/categoria.html',{'categoria':categoria,'entradas':entradas})
