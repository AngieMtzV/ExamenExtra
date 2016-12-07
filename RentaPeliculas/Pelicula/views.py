from django.shortcuts import render,redirect
from django.http import HttpResponse
from forms import PeliculaForm
from models import Pelicula



def pelicula_view(request):
	if request.method == 'POST':
		form = PeliculaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('lista_peliculas')
	else:
		form = PeliculaForm()

	return render(request,'pelicula_form.html', {'form':form})

def editar(request, pk):
	pelicula = Pelicula.objects.get(pk=pk)
	if request.method =="GET":
		form = PeliculaForm(instance=pelicula)
	else:
		form = PeliculaForm(request.POST, instance=pelicula)
		if form.is_valid():
			form.save()
		return redirect('lista_peliculas')
	return render(request, 'pelicula_form.html',{'form':form})

def listar(request):
	pelicula = Pelicula.objects.all()
	return render(request, 'lista_peliculas.html',{'peliculas':pelicula})

def eliminar(request,pk):
	pelicula = Pelicula.objects.get(pk=pk)
	pelicula.delete()
	return redirect('lista_peliculas')

def index(request):
	return render(request, 'index.html')