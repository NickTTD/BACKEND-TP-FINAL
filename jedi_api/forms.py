from django import forms

from jedi_api.models import UsuarioFuerza, Lightsaber, HabilidadFuerza


class ForceUserForm(forms.ModelForm):

    class Meta:
        model = UsuarioFuerza
        fields = [
            'name',
            'edad',
            'nacimiento',
            'sith',
            'HabilidadesDisponibles',
            'Sable',
        ]

class HabilidadFuerzaForm(forms.ModelForm):

    class Meta:
        model = HabilidadFuerza
        fields = [
            'name',
            'dificultad',
        ]
        
class LightsaberForm(forms.ModelForm):

    class Meta:
        model = Lightsaber
        fields = [
            'material',
            'año_creación',
            'color',
        ]