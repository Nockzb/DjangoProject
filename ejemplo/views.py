from django.shortcuts import render
from . import models
from datetime import date
from django.views import generic

# Create your views here.
def ejemplo(request):
    final = date(2024,4,1)
    hoy = date.today()
    diferencia=(final-hoy).days
    # segundo parametro es el path
    return render(request, "ejemplo.html", {"hoy":diferencia})

# def usuario(request):
#     datos = models.Datos.objects.all()   
#     usuario = datos[0]
    
#     context = {}    
#     context["id"] = usuario.id
#     context["nombre"] = usuario.nombre 
#     context["apellido1"] = usuario.apellido1
#     context["apellido2"] = usuario.apellido2
#     context["personas"] = datos # todos los datos de la BD
    
#     context["listaVacia"] = [] # lista vacía para que se muestre la imágen
    
    
#     context["texto"] = "Prueba argumento"
#     return render(request, "usuario.html", context)

class ListadoView(generic.ListView): 
    model = models.Datos
    template_name = "listado.html"
    
class DetalleView(generic.DetailView): 
    model = models.Datos 
    template_name = "detalle.html"
    
class CreateView(generic.CreateView):
    model = models.Datos
    # fields = ['nombre', 'apellido1', 'apellido2']
    template_name = "crear.html" 
    success_url = "/ejemplo/listado/" 

class UpdateView(generic.UpdateView):
    model = models.Datos
    # fields = ['nombre', 'apellido1', 'apellido2']
    template_name = "actualizar.html" 
    success_url = "/ejemplo/listado/"

class DeleteView(generic.DeleteView):
    model = models.Datos
    # fields = []
    template_name = "eliminar.html" 
    success_url = "/ejemplo/listado/"