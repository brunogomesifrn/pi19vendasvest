from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def galeria(request):
	return render(request, 'galeria.html')
def registro(request):
	return render(request, 'registro.html')
	
def login(request):
	return render(request, 'login.html')

def maquiagens(request):
	return render(request, 'maquiagens.html')

