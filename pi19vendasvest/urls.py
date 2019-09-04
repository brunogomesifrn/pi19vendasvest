
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path


from core.views import index, registro, galeria, login, maquiagens, perfumes

from core.views import index, registro, galeria, login, maquiagens,perfil

from core.views import index, registro, galeria, maquiagens
from django.contrib.auth import views as auth_views


urlpatterns = [
   	path('', index, name='index'),
   	path('galeria/',galeria, name="galeria"),
    path('maquiagens/',maquiagens, name="maquiagens"),
    path('perfumes/',perfumes, name="perfumes"),
    path('perfil/', perfil, name='perfil'),
    #registro de usuário
    path('login/', auth_views.LoginView.as_view(), name='login'),
	  #registro de usuário
    path('registro/', registro, name='registro')

   	

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
