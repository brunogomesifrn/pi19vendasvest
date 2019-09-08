from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

@login_required	
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

@login_required	
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

