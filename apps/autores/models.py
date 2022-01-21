from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200, blank=True, null=True)
    apellido_materno = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre
