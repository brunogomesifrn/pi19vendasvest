from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
def index(request):
	return render(request, 'index.html')

def galeria(request):
	return render(request, 'galeria.html')
	
def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form':form
	}
	return render(request, 'registro.html', contexto)
	
def login(request):
	return render(request, 'login.html')

def maquiagens(request):
	return render(request, 'maquiagens.html')


def perfumes(request):
	return render(request, 'perfumes.html')


def perfil(request):
	return render(request, 'perfil.html')


def vestuarios(request):
	return render(request, 'vestuarios.html')


