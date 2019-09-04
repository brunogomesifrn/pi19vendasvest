
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import index, registro, galeria, login, maquiagens, perfumes, vestuarios, perfil

<<<<<<< HEAD
=======

from core.views import index, registro, galeria, login, maquiagens, perfumes

from core.views import index, registro, galeria, login, maquiagens,perfil

from core.views import index, registro, galeria, maquiagens
>>>>>>> 7c986fb6a5e150e6ffd7575956757ff00eab2b72
from django.contrib.auth import views as auth_views


urlpatterns = [
   	path('', index, name='index'),
   	path('galeria/',galeria, name="galeria"),
    path('maquiagens/',maquiagens, name="maquiagens"),
    path('perfumes/',perfumes, name="perfumes"),
<<<<<<< HEAD
   	path('perfil/', perfil, name='perfil'),
    path('vestuarios/', vestuarios, name='vestuarios'),


   	#registro de usuário

=======
    path('perfil/', perfil, name='perfil'),
    #registro de usuário
>>>>>>> 7c986fb6a5e150e6ffd7575956757ff00eab2b72
    path('login/', auth_views.LoginView.as_view(), name='login'),
	  #registro de usuário
    path('registro/', registro, name='registro')

   	

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
