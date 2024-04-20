    
from django.db import models

class Alumno(models.Model):
    carnet = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Pago(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    numero_boleta = models.CharField(max_length=50)
    codigo_banco = models.CharField(max_length=20)
    fecha_pago = models.DateField()