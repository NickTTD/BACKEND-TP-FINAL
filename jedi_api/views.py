from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from jedi_api.serializers import UsuarioFuerzaSerializer, LightsaberSerializer, HabilidadFuerzaSerializer
from jedi_api.models import UsuarioFuerza, HabilidadFuerza, Lightsaber
from .forms import ForceUserForm, LightsaberForm, HabilidadFuerzaForm
from django.middleware.csrf import get_token
# Create your views here.

#def index(request):
   # return render(request, 'index.html')

def get_all_forceUsers():
    forceUsers = UsuarioFuerza.objects.all().order_by('name')
    forceUsers_serializers = UsuarioFuerzaSerializer(forceUsers, many=True)
    return forceUsers_serializers.data

def get_all_Lightsabers():
    Lightsabers = Lightsaber.objects.all().order_by('material')
    Lightsaber_serializers = LightsaberSerializer(Lightsabers, many=True)
    return Lightsaber_serializers.data

def get_all_habilidadesFuerza():
    habilidadesFuerza = HabilidadFuerza.objects.all().order_by('name')
    habilidadesFuerza_serializers = HabilidadFuerzaSerializer(habilidadesFuerza, many=True)
    return habilidadesFuerza_serializers.data



def usuarioFuerza_rest(request):
    usuariosFuerza = get_all_forceUsers()
    return JsonResponse(usuariosFuerza, safe=False)

def Lightsabers_rest(request):
    Lightsabers = get_all_Lightsabers()
    return JsonResponse(Lightsabers, safe=False)

def Habilidades_rest(request):
    habilidadesFuerza = get_all_habilidadesFuerza()
    return JsonResponse(habilidadesFuerza, safe=False)

def index_jedi(request):
    forceUsers = get_all_forceUsers()
    lightsabers = get_all_Lightsabers()
    habilidades = get_all_habilidadesFuerza()
    return render(request, 'index_jedi.html', {'forceUsers': forceUsers, 'Lightsabers': lightsabers, 'Habilidades': habilidades})

class forceUserFormView(CreateView):
    form_class = ForceUserForm
    template_name = 'force_form.html'
    success_url = '/'

    
class LightsaberFormView(CreateView):
    form_class = LightsaberForm
    template_name = 'lightsaber_form.html'
    success_url = '/'

class HabilidadFuerzaFormView(CreateView):
    form_class = HabilidadFuerzaForm
    template_name = 'habilidadFuerza_form.html'
    success_url = '/'

def index(request):
    forceUsers = get_all_forceUsers()
    lightsabers = get_all_Lightsabers()
    habilidades = get_all_habilidadesFuerza()
    
    context = {
        'forceUsers': forceUsers,
        'Lightsabers': lightsabers,
        'Habilidades': habilidades,
    }
    
    return render(request, 'index.html', context)