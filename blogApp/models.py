from django.db import models
# importamos la clase User
from django.contrib.auth.models import User

# Create your models here.

# CLASE PARA LAS CATEGORIAS
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='modificado')

    class Meta:
        verbose_name='categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

# CLASE PARA LOS POST
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='blog',null=True, blank=True)
    #  relacionamos el autor con la base de usuarios y le indicamos que si se elimina el usuario se eliminan los post
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # un post puede tener varias categorias 
    categorias =models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='modificado')

    class Meta:
        verbose_name='post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo
    