from django import forms
from .models import Tareas

class Tareas_Form(forms.ModelForm):
    class Meta:
        model=  Tareas
        fields= '__all__'    