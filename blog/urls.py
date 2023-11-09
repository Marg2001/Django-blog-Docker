
from django.urls import path
from .views import *
#from .views import home, generales1, programacion, videojuegos,tecnologia, tutoriales

urlpatterns = [
    path('', home, name= 'index'),
    path('generales1/', generales1, name= 'generales1'),
    path('programacion/', programacion, name= 'programacion'),
    path('videojuegos/', videojuegos, name= 'videojuegos'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('tutoriales/', tutoriales, name= 'tutoriales'),
    path('<slug:slug>/',detallePost, name = 'detalle_post'),
]