from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=3)
    sexo = models.CharField(max_length=10)
    materia = models.CharField(max_length=50)

def _str_ (self):
    return self.nome
    
