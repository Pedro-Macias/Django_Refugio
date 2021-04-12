from django import forms



class FormContacto(forms.Form):
    nombre = forms.CharField(label= 'Nombre',required=True, widget=forms.TextInput(
        attrs={'class':'form-control my-2','placeholder': 'Nombre'}
    ))
    email = forms.EmailField(label = 'Email',required=True,widget=forms.EmailInput(
        attrs={'class':'form-control my-2','placeholder': 'Email'}
    ))
    contenido = forms.CharField(label = 'Mensaje',required=True, widget=forms.Textarea(
        attrs={'class':'form-control my-2',  'placeholder': 'deja tu Comentario','rows':4}
    ))

    