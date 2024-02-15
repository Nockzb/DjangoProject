from django.db import models

class Datos(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    apellido1 = models.CharField(max_length = 50, verbose_name = "Primer apellido")
    apellido2 = models.CharField(max_length = 50, verbose_name = "Segundo apellido", blank = True, null = True)
    # jefe = models.ForeignKey('self', on_delete = models.SET_NULL, blank = True, null = True)
        
    class Meta:        
        verbose_name_plural = "Datos"
        def __str__(self):
            return f"{self.nombre} {self.apellido1} {self.apellido2}"
