from django.shortcuts import render , HttpResponse, redirect
from django.urls import reverse

# importar el archivo forms
from .forms import FormContacto
# importar EmailMessage
from django.core.mail import EmailMessage

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
            
            # enviar EMAIL
            # mensaje , el nombre de quien envia , el email de quien envie y el contenido
            # de quien viene y la cuenta de la que viene
            # si le quieres contestar
            email =EmailMessage('mensaje desde aplicacion refugio','El usuario con nombre {} con el mail {} te envia: \n\n {}'
            .format(nombre, email,contenido),'',['pin@pin.com'], reply_to=[email])

            try:
                email.send()   
                # enviar un parametro para que si todo va bien reciba un mensaje
                return redirect(reverse('Contacto')+'?ok')
            except:
                return redirect(reverse('Contacto')+'?fail')         

    return render (request,'contactoApp/contacto.html', {'form_Contacto':formulario_contacto})