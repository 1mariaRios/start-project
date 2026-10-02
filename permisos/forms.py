from django import forms
from .models import Permisos

class Permisos_form(forms.ModelForm):
    class Meta:
      model= Permisos
      fields= '__all__'