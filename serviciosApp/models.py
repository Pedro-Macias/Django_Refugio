from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=100)
        # con el parametro upload_to , le indicamos que las imagenes las guarde en media en la carpeta servicios
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='modificado')

    class Meta:
        verbose_name='servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo
    