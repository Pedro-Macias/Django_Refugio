from django.urls import path, include

# importamos las vistas
from refugioApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('servicios', views.servicios, name='Servicios'),
    path('refugio', views.refugio, name='Refugio'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),
]

# indicar la url para ver las imagenes 
urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)