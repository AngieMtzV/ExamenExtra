from django.test import TestCase

from django.test import TestCase
from Renta.models import Renta

class ProbarVista(TestCase):

    def test_ProbarTemplateAgregarRenta(self):
        response=self.client.get("/rentas/nueva")
        self.assertTemplateUsed(response,'renta_form.html')

    def test_ProbarTemplateListarRentas(self):
        response=self.client.get("/rentas/lista/")
        self.assertTemplateUsed(response,'lista_renta.html')

    