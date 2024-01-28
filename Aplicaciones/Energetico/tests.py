import unittest
from django.test import TestCase
from .models import Electrodomestico

# Create your test here.

class ElectrodomesticoTests(TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        Electrodomestico.objects.create(codigo='123456', nombre='Lavadora', consumo=100)

    def test_electrodomestico_str_method(self):
        # Verifica que el método __str__ devuelve el formato esperado
        electrodomestico = Electrodomestico.objects.get(codigo='123456')
        self.assertEqual(str(electrodomestico), 'Lavadora (100)')

    def test_electrodomestico_attributes(self):
        # Verifica que los atributos de Electrodomestico se guardan correctamente
        electrodomestico = Electrodomestico.objects.get(codigo='123456')
        self.assertEqual(electrodomestico.codigo, '123456')
        self.assertEqual(electrodomestico.nombre, 'Lavadora')
        self.assertEqual(electrodomestico.consumo, 100)

