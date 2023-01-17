from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from .models import Datos

# Create your views here.
class HomeViewTemplate(TemplateView):
    template_name= 'agenda.html'
    model = Datos

def mostrarDatos(request):
    listData = list(Datos.objects.values())
    return JsonResponse(listData, safe=False)


