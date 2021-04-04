from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request):
    return render (request,'refugioApp/home.html')

def servicios(request):
    return render (request,'refugioApp/servicios.html')

def refugio(request):
    return render (request,'refugioApp/refugio.html')

def blog(request):
    return render (request,'refugioApp/blog.html')

def contacto(request):
    return render (request,'refugioApp/contacto.html')