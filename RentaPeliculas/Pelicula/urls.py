from django.conf.urls import url
from Pelicula.views import pelicula_view, eliminar, listar,editar,index

urlpatterns = [
    url(r'^nueva$',pelicula_view, name='pelicula_nueva'),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', eliminar, name='eliminar_pelicula'),
    url(r'lista/', listar, name='lista_peliculas'),
    url(r'^(?P<pk>[0-9]+)/modificar/$',editar, name='editar_pelicula'),
     url(r'^index', index , name='index'),
   
]