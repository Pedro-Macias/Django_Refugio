from django.urls import path, include

# importamos las vistas
from refugioApp import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('servicios', views.servicios, name='Servicios'),
    path('refugio', views.refugio, name='Refugio'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),
]