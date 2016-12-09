from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from Pelicula.models import Pelicula,Clas,Genero,Actores
from Pelicula.forms import PeliculaForm
from . import models

class ProbarVista(TestCase):

    def test_ProbarIndexTemplate(self):
        response=self.client.get("/peliculas/index")
        self.assertTemplateUsed(response,'index.html')


    def test_ProbarTemplateAgregarPelicula(self):
        response=self.client.get("/peliculas/nueva")
        self.assertTemplateUsed(response,'pelicula_form.html')

    def test_ProbarTemplateListarPelicula(self):
        response=self.client.get("/peliculas/lista/")
        self.assertTemplateUsed(response,'lista_peliculas.html')

    
    def test_eliminar_pelicula_post(self):
    	peliTot = Pelicula.objects.all()
    	total = peliTot.count()
    	pelicula = Pelicula()
    	pelicula.titulo = "Pruebame Esta"
    	pelicula.sinopsis = "Angie Reprueba Testing"
    	clasificacion = Clas.objects.create(
			clas="B-15",
			)
    	pelicula.clasificacion=clasificacion
    	pelicula.duracion="Toda la vida"
    	gene = Genero.objects.create(
    		genero="TragiComedia",
    		)
    	pelicula.genero = gene
    	pelicula.estreno = True
    	pelicula.save()
    	actor1 = Actores.objects.create(
    		nombre="Angie",
    		)
    	actor2 = Actores.objects.create(
    		nombre="Amgdark",
    		)
    	actor3 = Actores.objects.create(
    		nombre="Brenda",
    		)
    	pelicula.actores = actor1,actor2,actor3
    	pelicula.rentada = False
    	pelicula.save()
    	self.assertEquals(pelicula.id, 1)
    	self.assertEqual(Pelicula.objects.count(), total + 1)
    	self.assertEqual(Pelicula.objects.first().sinopsis, 'Angie Reprueba Testing')
        self.client.post(
			'/peliculas/%d/eliminar/' % (Pelicula.objects.first().id))
    	#self.assertEqual(pelicula.objects.count(), 0)


class PruebaFormulario(TestCase):

	def test_addPelicula(self):
		peliTot = Pelicula.objects.all()
		total = peliTot.count()
		pelicula = Pelicula()
		pelicula.titulo = "Tu gfa"
		pelicula.sinopsis = "Tu gfa se enperra por que no pasaste Testing"
		clasificacion = Clas.objects.create(
			clas="B-15",
			)
		pelicula.clasificacion=clasificacion
		pelicula.duracion="Toda la vida"
		gene = Genero.objects.create(
			genero="TragiComedia",
			)
		pelicula.genero = gene
		pelicula.estreno = True
		#pelicula.estreno = estreno.objects.bool(True)
		#estreno = e
		pelicula.save()
		actor1 = Actores.objects.create(
			nombre="La gfa chida",
			)
		actor2 = Actores.objects.create(
			nombre="El gf chido",
			)
		actor3 = Actores.objects.create(
			nombre="Pancho Cachondo",
			)
		pelicula.actores = actor1,actor2,actor3
		#r = rentada.objects.bool(False)
		pelicula.rentada = False
		pelicula.save()
		totalNuevo= Pelicula.objects.all()
		self.assertEqual(total+1,totalNuevo.count())

