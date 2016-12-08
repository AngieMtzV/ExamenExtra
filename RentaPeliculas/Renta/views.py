from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse
from forms import RentaForm
from models import Renta



def renta_view(request):
	if request.method == 'POST':
		form = RentaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('lista_renta')
	else:
		form = RentaForm()

	return render(request,'renta_form.html', {'form':form})

def editar_renta(request, pk):
	renta = Renta.objects.get(pk=pk)
	if request.method =="GET":
		form = RentaForm(instance=renta)
	else:
		form = RentaForm(request.POST, instance=renta)
		if form.is_valid():
			form.save()
		return redirect('lista_renta')
	return render(request, 'renta_form.html',{'form':form})

def listar_renta(request):
	renta = Renta.objects.all()
	return render(request, 'lista_renta.html',{'rentas':renta})

def eliminar_renta(request,pk):
	renta = Renta.objects.get(pk=pk)
	renta.delete()
	return redirect('lista_renta')

def index(request):
	return render(request, 'index.html')