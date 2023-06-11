from django.urls import path
from . import views

urlpatterns = [
    #rutas en el homepage
    path('', views.index, name='index'),
    path('sobreNosotros', views.about, name='sobreNosotros'),
    path('ventajas', views.advantages, name='ventajas'),
    path('contactanos', views.contact, name='contactanos'),
    path('funciones', views.functions, name='funciones'),
    path('login', views.login, name='login'),
    path('modulos', views.modules, name='modulos'),
    path('rec_pass', views.rec_pass, name='rec_pass'),
    path('inicio', views.index, name='inicio'),
        #Rutas en la aplicacion
    path('incioApp', views.inicioApp, name='inicioApp'),
    path('registrarVehiculo', views.registrarVehiculo, name='registrarVehiculo'),
    
]
 