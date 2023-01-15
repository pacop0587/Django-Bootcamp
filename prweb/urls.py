from django.contrib import admin
from django.urls import path
from agenda.views import HomeViewTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeViewTemplate.as_view())
]
