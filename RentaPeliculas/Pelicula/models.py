from __future__ import unicode_literals

from django.db import models

class Clas(models.Model):
	clas = models.CharField(u'Clasificacion', max_length=10)

	def __unicode__(self):
		return self.clas

class Genero(models.Model):
	genero = models.CharField(u'Genero',max_length=150)

	def __unicode__(self):
		return self.genero

class Actores(models.Model):
	nombre = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nombre



class Pelicula(models.Model):
	titulo = models.CharField(u'Titulo', max_length=200)
	sinopsis = models.CharField(u'Sinopsis',max_length=350)
	clasificacion = models.OneToOneField(Clas, null=False, unique=True, on_delete=models.CASCADE)
	duracion = models.CharField(u'Duracion', max_length=50)
	genero = models.OneToOneField(Genero, null=False, unique=True, on_delete=models.CASCADE)
	estreno = models.BooleanField()
	actores = models.ManyToManyField(Actores)
	rentada = models.BooleanField(default=False)

	def __unicode__(self):
		return self.titulo


