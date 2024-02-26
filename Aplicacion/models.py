from django.db import models

class Meta:
    app_label = 'Aplicacion'

class Persona(models.Model):
    ESTADOS_ACTIVIDAD = (
        ('conectado', 'Conectado'),
        ('ausente', 'Ausente'),
        ('desconectado', 'Desconectado'),
    )
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    nombre_usuario = models.CharField(max_length = 255)
    estado_actividad = models.CharField(max_length=20, choices=ESTADOS_ACTIVIDAD, default='conectado')
    correo = models.EmailField()
    contrasenia = models.CharField(max_length = 255)
    
    def sesion(self):
        return True
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Admin(Persona):
    
    def gestionar_usuario(self):
        return True
    
    def agregar_electrodomestico(self):
        return True
    
    def eliminar_electrodomestico(self):
        return True
    
    def modificar_electrodomestico(self):
        return True
    
class Usuario(Persona):
    
    def gestionar_perfil(self):
        return True
    
class Medidor(models.Model):
    nombre = models.CharField(max_length = 255)
    tipo_medicion = models.CharField(max_length = 255)
    maximo_consumo = models.DecimalField(max_digits=5, decimal_places=2)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def obtener_reporte(self):
        return 0.0
    
class Electrodomestico(models.Model):
    CATEGORIAS = (
        ('pequeños', 'Pequeños'),
        ('medianos', 'Medianos'),
        ('grandes', 'Grandes'),
    )
    codigo = models.CharField(primary_key = True, max_length = 8)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='pequeños')
    imagen = models.ImageField(upload_to='electrodomesticos/')
    nombre = models.CharField(max_length = 255)
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    consumo = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=1)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre} {self.precio} ({self.codigo})"
    
