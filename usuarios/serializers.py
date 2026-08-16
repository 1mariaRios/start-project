from rest_framework import serializers
from tareas.models import Perfil

class PerfilSerializers(serializers.serializer):
    class Meta:
        model = Perfil
        fields = "__all__"