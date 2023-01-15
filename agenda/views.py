from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def viewTemplate(request):

#     return render(request, '../templates/agenda.html')

class HomeViewTemplate(TemplateView):
    template_name= 'agenda.html'

    # def get(self, request):
    #     return HttpResponse(self.template_view)
