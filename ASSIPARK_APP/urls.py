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
    path('inicioApp', views.inicioApp, name='inicioApp'),
    path('registrarVehiculo', views.registrarVehiculo, name='registrarVehiculo'),
    path('descripcion', views.description, name='descripcion'),
    path('eliminar/<int:idParametro>', views.eliminar, name='eliminar'),
    path('editar', views.editar, name='editar'),
    path('vehiculo/editar/<int:idParametro>', views.editar, name='editar'),
    #Rutas de contacto
    path('KevinGit', views.kevinGit, name='KevinGit'),
    path('LeninGit', views.leninGit, name='LeninGit'),
    path('DavidGit', views.davidGit, name='DavidGit'),
    path('AngelGit', views.angelGit, name='AngelGit'),
    
    
]