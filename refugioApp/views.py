from django.shortcuts import render , HttpResponse

# importar los servicios desde la app servicioApp

# Create your views here.

def home(request):
    return render (request,'refugioApp/home.html')


def refugio(request):
    return render (request,'refugioApp/refugio.html')

def blog(request):
    return render (request,'refugioApp/blog.html')

def contacto(request):
    return render (request,'refugioApp/contacto.html')