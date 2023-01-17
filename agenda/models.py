from django.db import models

# Create your models here.
class Datos(models.Model):
    namePerson = models.CharField(max_length=50)
    emailPerson = models.CharField(max_length=50)

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)