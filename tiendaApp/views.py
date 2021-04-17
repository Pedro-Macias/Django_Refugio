from django.shortcuts import render , HttpResponse

# importar los servicios desde la app servicioApp

# Create your views here.

def tienda(request):
    return render (request,'tiendaApp/tienda.html')