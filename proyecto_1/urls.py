from django.contrib import admin
from django.urls import include, path

from holaMundo import views
urlpatterns = [
    path('', views.hola_mundo),
    path('admin/', admin.site.urls),
    path('hola',views.hola_mundo),
    path("ejemplo/", include("ejemplo.urls", namespace="ejemplo"))
]