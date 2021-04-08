from django.urls import path, include

# importamos las vistas
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios, name='Servicios'),

]
