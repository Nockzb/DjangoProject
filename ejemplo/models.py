from django.db import models

# Create your models here.
class Datos(models.Model): 
    id = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=50) 
    apellido1 = models.CharField(max_length=50, verbose_name="Primer apellido") 
    apellido2 = models.CharField(max_length=50, verbose_name="Segundo apellido", blank=True, null=True)
    
    class Meta:        
        verbose_name_plural = "Datos"
