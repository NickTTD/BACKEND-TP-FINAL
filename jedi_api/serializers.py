from rest_framework import serializers

from jedi_api.models import UsuarioFuerza,Lightsaber,HabilidadFuerza


class UsuarioFuerzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioFuerza
        fields = '__all__'

class LightsaberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lightsaber
        fields = '__all__'

class HabilidadFuerzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadFuerza
        fields = '__all__'