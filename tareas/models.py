from django.db import models
from usuarios.models import Perfil
actividades={
    's_generales': 'auxiliar de servicios generales',
    'jardineria': 'Realizar actividades de jardineria',
    'electricista': 'electrico',
    'ornamentacion': 'Trabajos de ornamentacion',
    'a_techos':'Arreglo de techos',
    'pintura':'Labores de pintura',
    'rastrillo':'realizar actividades de rastrillo',
    'evento':'Realizar apoyo en evento',
    'vidrios':'Realizar limpieza de vidrios'
}

estado={
    'pendiente':'Pendiente',
    'e_proceso':'En proceso',
    'culminada':'Tarea Finalizada'
}

class Tareas(models.Model):
    actividad=models.CharField(choices=actividades, default='s_generales')
    encargado=models.OneToOneField(Perfil, on_delete=models.CASCADE, null=False)
    descripcion=models.CharField(max_length=600, null=False)
    estado=models.CharField(choices=estado, default="p_hacer")
    
    
    def __str___(self):
        return self.encargado, self.descripcion, self.actividad