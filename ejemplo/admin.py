from django.contrib import admin
from .models import Datos


# Register your models here.
@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    model = Datos
    list_display = ["nombre", "apellido1", "apellido2"]
    search_fields = ["nombre", "apellido1"]

