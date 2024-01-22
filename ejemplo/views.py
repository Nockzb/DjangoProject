from django.shortcuts import render
from . import models
from datetime import date

# Create your views here.
def ejemplo(request):
    final = date(2024,4,1)
    hoy = date.today()
    diferencia=(final-hoy).days
    # segundo parametro es el path
    return render(request,"ejemplo.html",{"hoy":diferencia})

def usuario(request):
    datos = models.Datos.objects.all()
    usuario = datos[0]
    
    context = {}
    context["id"] = usuario.id
    context["nombre"] = usuario.nombre
    context["apellido1"] = usuario.apellido1
    context["apellido2"] = usuario.apellido2
    
    return render(request, "usuario.html", context)
    