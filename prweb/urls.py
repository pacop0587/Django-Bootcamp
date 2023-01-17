from django.contrib import admin
from django.urls import path
from agenda.views import HomeViewTemplate, mostrarDatos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeViewTemplate.as_view()),
    path('datos/',mostrarDatos)
]
