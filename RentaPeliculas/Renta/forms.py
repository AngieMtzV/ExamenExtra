from django import forms
from models import Renta

class RentaForm(forms.ModelForm):
	
	class Meta:
		model = Renta

		fields = (
			'registro',
			'usuario',
			'pelicula',
			'fecha_entrega',
			'genero',
			)
		
class RentaEdit(forms.ModelForm):

	class Meta:
		model = Renta

		fields = (
			'registro',
			'usuario',
			'pelicula',
			'fecha_entrega',
			'genero',
			)