from django.shortcuts import render

from serviciosApp.models import Servicio
# Create your views here.


def servicios(request):
    # en una variable recuperamos todos los objetos que tengo dentro de la clase Servicio
    servicios = Servicio.objects.all()
    # incluir los servicios importados
    return render (request,'serviciosApp/servicios.html',{'servicios':servicios})
