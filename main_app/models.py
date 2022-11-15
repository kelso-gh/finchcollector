from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    threats = models.TextField(max_length=100) #text box!
    