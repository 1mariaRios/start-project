from django.db import models
from django.contrib.auth.models import User


rol={
    's_generales': 'auxiliar de servicios generales',
    'electricista':'Actividades de electricidad',
    'Jardinero':'Realizar actividades de jardineria',
    'RESPEL':'Realizar actividades de recoleccion de residuos peligrosos',
    'reciclaje':'Realizar actividades de reciclaje',
    'plomero':'Realizar actividades de plomeria',
    'aux_c_taller':'Auxiliar de casa taller'
    
}

style_flow={
    'dark':'pink, purple, black',
    'claro':'purple, blue'
}

class Perfil(models.Model):
    nombre=models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    n_documento=models.IntegerField()
    r_fisica=models.BooleanField(default=False, null=True)
    firma=models.ImageField(null=False)
    zona_encargada=models.CharField(max_length=250, null=True)
    rol=models.CharField(choices=rol, default='s_generales', null=True)
    clave=models.IntegerField()
    apariencia=models.CharField(choices=style_flow, default='claro')
    c_alturas=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nombre
    

    
    
