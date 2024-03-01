from django.db import models

# Create your models here.

class FuenteEnergiaExterna(models.Model):
    tipo = models.CharField(max_length = 255)
    capacidad = models.DecimalField(max_digits=5, decimal_places=2)
    generar_electricidad = models.DecimalField(max_digits=5, decimal_places=2)

    def generar_electricidad(self):
        return self.generar_electricidad

class PanelSolar(models.Model):
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)

    def obtener_generacion(self):
        return self.obtener_generacion

class Eólico(models.Model):
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)

    def obtener_generacion(self):
        return self.obtener_generacion
