from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    return HttpResponse("Hola Mundo")