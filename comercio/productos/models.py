from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    tipo=models.CharField(max_length=100, null=True)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=255)
    observaciones = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)