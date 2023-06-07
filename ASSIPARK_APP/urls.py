from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobreNosotros', views.about, name='sobreNosotros'),
    path('ventajas', views.advantages, name='ventajas'),
    path('contactanos', views.contact, name='contactanos'),
    path('funciones', views.functions, name='funciones'),
    path('login', views.login, name='login'),
    path('modulo_1', views.module_1, name='modulo_1'),
    path('modulos', views.modules, name='modulos'),
    path('rec_pass', views.rec_pass, name='rec_pass'),
    path('inicio', views.index, name='inicio')
]
 