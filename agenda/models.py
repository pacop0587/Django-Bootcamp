from django.db import models

# Create your models here.
class Datos(models.Model):
    namePerson = models.CharField(max_length=50)
    emailPerson = models.CharField(max_length=50)
