from rest_framework import serializers
from .models import Permisos

class PermisoSerializer(serializers.serializer):
    class Meta:
        model=Permisos
        fields="__all__"