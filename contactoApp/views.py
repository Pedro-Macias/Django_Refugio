from django.shortcuts import render , HttpResponse, redirect
from django.urls import reverse

# importar el archivo forms
from .forms import FormContacto

# Create your views here.




def contacto(request):
    formulario_contacto = FormContacto()
    # si se ha enviado informacion y es valido
    if request.method=='POST':
        formulario_contacto= FormContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')

            # enviar un parametro para que si todo va bien reciba un mensaje
            return redirect(reverse('Contacto')+'?ok')          

    return render (request,'contactoApp/contacto.html', {'form_Contacto':formulario_contacto})