from django.shortcuts import render , HttpResponse

# importar el archivo forms
from .forms import FormContacto

# Create your views here.




def contacto(request):
    formulario_contacto = FormContacto()
    return render (request,'contactoApp/contacto.html', {'form_Contacto':formulario_contacto})