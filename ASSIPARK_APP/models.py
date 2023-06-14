from django.db import models
from typing import Any, Dict, Tuple
# Create your models here.

class Vehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    placa=models.TextField(verbose_name='Placa', max_length=10)
    color=models.CharField(verbose_name='Color', max_length=15)
    marca=models.CharField(verbose_name='Marca', max_length=15)
    tipo=models.CharField(verbose_name='Tipo de Vehiculo', max_length=10)
    parqueadero=models.CharField(verbose_name='Parqueadero Asignado', max_length=5)
    propietario=models.CharField(verbose_name='Nombre del propietario', max_length=50)
    cedula=models.CharField(verbose_name='Identificaion del propietario', max_length=12)
    telefono=models.CharField(verbose_name='Telefono del propietario', max_length=10)
    apartamento=models.CharField(verbose_name='Apartamento', max_length=7)
    tipoPropietario=models.CharField(verbose_name='¿Visitante o residente?', max_length=10)
    
    def delete(self, using=None, keep_parents=False):
        super().delete()

