from django.db import models


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    trabajo = models.CharField(max_length=50, default="")
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length= 200,unique=True)
    departamento = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido} {self.trabajo}"
    
    
