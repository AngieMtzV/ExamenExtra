from django.contrib import admin
from Pelicula.models import Pelicula,Clas,Genero,Actores
# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Clas)
admin.site.register(Genero)
admin.site.register(Actores)