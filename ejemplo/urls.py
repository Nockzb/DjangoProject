from django.urls import path
from . import views

app_name="ejemplo"
urlpatterns = [
    path('', views.ejemplo),
    path('usuario/', views.usuario),    
]