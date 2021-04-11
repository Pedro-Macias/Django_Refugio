from django import forms



class FormContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True , max_length=100)
    email = forms.EmailField(label='Email', required=True , max_length=100)
    contenido = forms.CharField(label='Contenido', max_length= 200)

    