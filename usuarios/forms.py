from django import forms
from .models import Perfil

class Perfil_Form(forms.ModelForm):
    class Meta:
        model= Perfil
        fields= '__all__'