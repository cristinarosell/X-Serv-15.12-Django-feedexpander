from django.db import models

# Create your models here.

class Persona(models.Model):
    name = models.CharField(max_length = 30)
    
class Tweet(models.Model):
    content = models.CharField(max_length = 150)
    url = models.CharField(max_length = 64)
    name = models.ForeignKey(Persona)


