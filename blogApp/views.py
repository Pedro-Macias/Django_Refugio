from django.shortcuts import render
from blogApp.models import Post

# Create your views here.

def blog(request):
    # en una variable recuperamos todos los objetos que tengo dentro de la clase Servicio
    entradas= Post.objects.all()
    return render (request,'blogApp/blog.html',{'entradas':entradas})

