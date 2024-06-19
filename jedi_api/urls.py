from django.urls import path
from jedi_api import views

urlpatterns = [
    path('', views.index, name=''),
    path('index_jedi', views.index_jedi, name='index_jedi'),
    path('usuarioFuerza_rest/', views.usuarioFuerza_rest, name='usuarioFuerza_rest'),
    path('lightsabers_rest/', views.Lightsabers_rest, name='lightsaber_rest'),
    path('Habilidades_rest/', views.Habilidades_rest, name='Habilidades_rest'),
    path('force_form/', views.forceUserFormView.as_view(), name='force_form'),
    path('lightsaber_form/', views.LightsaberFormView.as_view(), name='lightsaber_form'),
    path('habilidadFuerza_form/', views.HabilidadFuerzaFormView.as_view(), name='habilidad_form'),
]