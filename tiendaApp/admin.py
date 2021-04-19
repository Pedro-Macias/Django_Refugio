from django.contrib import admin

from .models import  CategoriaProducto, Producto


# ver campos ocultos
class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

# Register your models here.
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
