from django.db import models

# Create your models here.

class Speciality(models.Model):
    CodePS = models.CharField("Код ПС",max_length=2)
    FullCode = models.CharField("Полный Код",max_length=6)
    Name = models.CharField("Наименование",max_length=300)
    RegNumber = models.CharField("Регистрационный номер",max_length=20)
    Description = models.TextField("Основная цель вида профессиональной деятельности")
    OccupationGroup = models.ManyToManyField("Группа занятий")
    EconomicActivity = models.ManyToManyField("Виды экономической деятельности")

class OccupationGroup(models.Model):
    CodeOKZ = models.CharField("Код ОКЗ",max_length=4)
    Name = models.CharField("Наименование",max_length=300)

class EconomicActivity(models.Model):
    CodeOKVED = models.CharField("Код ОКВЭД",max_length=10)
    Name = models.CharField("Наименование",max_length=300)