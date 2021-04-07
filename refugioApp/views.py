from django.shortcuts import render , HttpResponse

# importar los servicios desde la app servicioApp
from serviciosApp.models import Servicio
# Create your views here.

def home(request):
    return render (request,'refugioApp/home.html')

def servicios(request):
    # en una variable recuperamos todos los objetos que tengo dentro de la clase Servicio
    servicios = Servicio.objects.all()
    # incluir los servicios importados
    return render (request,'refugioApp/servicios.html',{'servicios':servicios})

def refugio(request):
    return render (request,'refugioApp/refugio.html')

def blog(request):
    return render (request,'refugioApp/blog.html')

def contacto(request):
    return render (request,'refugioApp/contacto.html')