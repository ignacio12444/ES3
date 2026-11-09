from django.db import models


class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    rut = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    anio_nacimiento = models.IntegerField()
    especie = models.CharField(max_length=50)
    responsable = models.ForeignKey(
        Responsable,
        on_delete=models.CASCADE,
        related_name='mascotas'
    )

    def __str__(self):
        return self.nombre
