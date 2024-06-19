from django.db import models

# Create your models here.
#Las que cree yo.


class HabilidadFuerza(models.Model):
    name = models.CharField(max_length=128)
    class dificultad(models.TextChoices):  #No entiendo muy bien por que esto requiere 'ALGO = "Algo"' but oh
        FACIL = "Fácil"
        MEDIO = "Medio"
        DIFICIL = "Difícil"

    dificultad = models.CharField(max_length=20, choices=dificultad.choices, default='Fácil')
    def __str__(self):
        return f'{self.name}'
    

class Lightsaber(models.Model):
    material = models.CharField(max_length=128)
    año_creación = models.DateField()
    class Color(models.TextChoices):
        AZUL = 'Azul'
        VERDE = 'Verde'
        ROJO = 'Rojo'
        VIOLETA = 'Violeta'
        AMARILLO = 'Amarillo'

    color = models.CharField(max_length=20, choices=Color.choices, default='Azul')
    def __str__(self):
        return f'{self.material}, {self.color}, {self.año_creación}' if self.material and self.color and self.año_creación else str(self.id)

class UsuarioFuerza(models.Model):
    name = models.CharField(max_length=128)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    sith = models.BooleanField(default=False)
    HabilidadesDisponibles = models.ManyToManyField(HabilidadFuerza, blank=True)
    Sable = models.OneToOneField(Lightsaber, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.name}, {self.edad}, Sith?{self.sith}'