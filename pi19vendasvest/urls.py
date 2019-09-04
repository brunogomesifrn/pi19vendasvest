
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import index, registro, galeria, login, maquiagens, perfumes, vestuarios, perfil
<<<<<<< HEAD
=======

from core.views import index, registro, galeria, maquiagens
>>>>>>> a12b806fb98a07105a5f487d28f058576119af49
from django.contrib.auth import views as auth_views


urlpatterns = [
   	path('', index, name='index'),
   	path('galeria/',galeria, name="galeria"),
    path('maquiagens/',maquiagens, name="maquiagens"),
    path('perfumes/',perfumes, name="perfumes"),

   	path('perfil/', perfil, name='perfil'),
    path('vestuarios/', vestuarios, name='vestuarios'),


   	#registro de usuário
<<<<<<< HEAD


    path('perfil/', perfil, name='perfil'),
    #registro de usuário

=======
    path('perfil/', perfil, name='perfil'),
>>>>>>> a12b806fb98a07105a5f487d28f058576119af49
    path('login/', auth_views.LoginView.as_view(), name='login'),
	  #registro de usuário
    path('registro/', registro, name='registro')

   	

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
