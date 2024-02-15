from django import forms
from django.db import models


class DatosForm(forms.ModelForm):
    class Meta:
        model = models.Model
        fields = ["nombre", "apellido1", "apellido2"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "apellido1": forms.TextInput(attrs={"class":"form-control"}),
            "apellido2": forms.TextInput(attrs={"class":"form-control"}),
        }