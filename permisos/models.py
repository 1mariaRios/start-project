from django.db import models
from usuarios.models import Perfil

permiso={
    'bolsa':'Beneficio en tiempo de dia de bolsa',
    'cumpleaños': 'Beneficio en tiempo de dia cumpleaños',
    'matrimonio':'Beneficio en tiempo de matrimonio',
    'graduacion':'Beneficio de dia por graduacion',
    'vacaciones': 'Solicitar permiso disfrute vacaciones'
}
 
class Permisos(models.Model):
    solicitante=models.OneToOneField(Perfil, on_delete=models.CASCADE)
    permiso=models.CharField(choices=permiso, default="bolsa"),
    dia=models.IntegerField()
    aprobado=models.BooleanField(default=False)
    
    def __str__(self):
        return self.solicitante