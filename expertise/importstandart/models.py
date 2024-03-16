from django.db import models

# Create your models here.

class Speciality(models.Model):
    CodePS = models.CharField(max_length=2)
    FullCode = models.CharField(max_length=6)
    Name = models.CharField(max_length=300)
    RegNumber = models.CharField(max_length=20)
    Description = models.TextField()
    OccupationGroup = models.JSONField()
    EconomicActivity = models.JSONField()
