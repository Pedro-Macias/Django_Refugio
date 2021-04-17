from django.urls import path, include

# importamos las vistas
from . import views

urlpatterns = [
    path('', views.tienda, name='Tienda'),

]
