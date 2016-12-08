from django.test import TestCase
from tareas.models import Pelicula

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

    