from django.db import models

# Create your models here.

class Sample(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    dob = models.DateTimeField()