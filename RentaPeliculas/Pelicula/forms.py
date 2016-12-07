from django import forms
from models import Pelicula

class PeliculaForm(forms.ModelForm):
	
	class Meta:
		model = Pelicula

		fields = (
			'titulo',
			'sinopsis',
			'clasificacion',
			'duracion',
			'genero',
			'estreno',
			'actores',
			'rentada',
			)
		
class FamiliaEdit(forms.ModelForm):

	class Meta:
		model = Pelicula

		fields = (
			'titulo',
			'sinopsis',
			'clasificacion',
			'duracion',
			'genero',
			'estreno',
			'actores',
			'rentada',
			)