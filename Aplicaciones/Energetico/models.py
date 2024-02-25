from django.db import models

# Create your models here.

class Electrodomestico(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    consumo = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.consumo)
    
    class Meta:

        app_label = 'loginbeta'



class Admin(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=255)

    def permisos(self):
        return True

    def sesion(self):
        return True

    def crearLista(self):
        return True
    
    def gestionarUsuario(self):
        return True

    def agregarElemento(self):
        return True
    
    def removerElemento(self):
        return True

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=255)

    def sesion(self):
        return True

    def crearLista(self):
        return True

class Medidor(models.Model):
    nombre = models.CharField(max_length=255)
    tipoMedicion = models.CharField(max_length=255)
    datoConsumo = models.FloatField()

    def registrarConsumo(self):
        return 0.0

    def obtenerReporte(self):
        return 0.0

class AreaCasa(models.Model):
    nombreArea = models.CharField(max_length=255)
    listaElectrodomestico = models.CharField(max_length=255)

    def obtenerConsumo(self):
        return 0.0

class Casa(models.Model):
    tamaño = models.CharField(max_length=255)

    def obtenerConsumo(self):
        return 0.0

class CalculadoraCosto(Medidor):
    gastoEnergetico = models.FloatField()
    gastoMonetario = models.FloatField()

    def calcularCosto(self):
        return 0.0

    def generarGasto(self):
        return 0.0

class Estadistica(CalculadoraCosto):
    tiempo = models.CharField(max_length=255)

    def consumoTotal(self):
        return 0.0

    def prediccionConsumo(self):
        return 0.0

class Grafico(CalculadoraCosto):
    tipo = models.CharField(max_length=255)

    def generarGrafica(self):
        return True