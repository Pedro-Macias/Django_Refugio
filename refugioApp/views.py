from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home')

def servicios(request):
    return HttpResponse('Servicios')

def refugio(request):
    return HttpResponse('Refugio')

def blog(request):
    return HttpResponse('Blog')

def contacto(request):
    return HttpResponse('Contacto')