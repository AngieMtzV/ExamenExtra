from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from Pelicula.models import Pelicula,Genero



class Renta(models.Model):
	registro = models.DateTimeField()
	usuario = models.ForeignKey(User)
	pelicula = models.ManyToManyField(Pelicula)
	fecha_entrega = models.DateField()
	genero = models.OneToOneField(Genero, null=False, unique=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.usuario.first_name