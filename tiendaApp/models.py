from django.db import models

# Create your models here.

from django.db import models
# importamos la clase User
from django.contrib.auth.models import User

# Create your models here.

# CLASE PARA LAS CATEGORIAS
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='tienda',null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='modificado')

    class Meta:
        verbose_name='Categoria Producto'
        verbose_name_plural = 'Categorias de Productos'
    
    def __str__(self):
        return self.nombre

# CLASE PARA LOS PRODUCTOS
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='tienda',null=True, blank=True)
    precio = models.FloatField()
    disponibilidad =models.BooleanField(default=True)
    # un post puede tener varias categorias 
    categorias =models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='modificado')

    class Meta:
        verbose_name='Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.titulo
    