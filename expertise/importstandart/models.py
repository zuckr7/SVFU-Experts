from django.db import models
from rest_framework import routers,serializers,viewsets
# Create your models here.


class OccupationGroup(models.Model):
    CodeOKZ = models.CharField("Код ОКЗ",max_length=4)
    Name = models.CharField("Наименование",max_length=300)


class EconomicActivity(models.Model):
    CodeOKVED = models.CharField("Код ОКВЭД",max_length=10)
    Name = models.CharField("Наименование",max_length=300)


class WorkFunction(models.Model):
    Code = models.CharField()
    Name = models.CharField()
    Qualification = models.CharField()


class GeneralFunction(WorkFunction):
    PossibleJobs = models.ForeignKey()


class ParticularFunction(WorkFunction):
    pass


class ProfStandart(models.Model):
    Title = models.CharField("Наименование",max_length=300)
    RegNumber = models.CharField("Регистрационный номер",max_length=20)
    CodePS = models.CharField("Код ПС",max_length=15)
    Goal = models.TextField("Основная цель вида профессиональной деятельности")
    OccupationGroup = models.ManyToManyField(OccupationGroup, verbose_name="Группа занятий")
    EconomicActivity = models.ManyToManyField(EconomicActivity, verbose_name="Виды экономической деятельности")
    GeneralizedFunctions = models.ManyToManyField(GeneralFunction, verbose_name="Обобщенные трудовые функции")
