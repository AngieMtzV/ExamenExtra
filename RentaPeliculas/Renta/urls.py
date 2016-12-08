from django.conf.urls import url
from Renta.views import renta_view, eliminar_renta, listar_renta,editar_renta

urlpatterns = [
    url(r'^nueva$',renta_view, name='renta_nueva'),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', eliminar_renta, name='eliminar_renta'),
    url(r'lista/', listar_renta, name='lista_renta'),
    url(r'^(?P<pk>[0-9]+)/modificar/$',editar_renta, name='editar_renta'),
     
]