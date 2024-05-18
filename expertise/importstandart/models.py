from django.db import models
from rest_framework import routers,serializers,viewsets
# Create your models here.


# class OccupationGroup(models.Model):
#     codeOKZ = models.CharField("Код ОКЗ",max_length=4)
#     name = models.CharField("Наименование",max_length=300)


# class EconomicActivity(models.Model):
#     codeOKVED = models.CharField("Код ОКВЭД",max_length=10)
#     name = models.CharField("Наименование",max_length=300)

class ProfStandart(models.Model):
    title = models.CharField("Наименование",max_length=300)
    regNumber = models.CharField("Регистрационный номер",max_length=20)
    codePS = models.CharField("Код ПС",max_length=15)
    goal = models.TextField("Основная цель вида профессиональной деятельности")
    list_okz = models.JSONField("Группа занятий")
    list_okved = models.JSONField("Отнесение к видам ЭД")

    
class WorkFunction(models.Model):
    code = models.CharField("Код",max_length=50)
    name = models.CharField("Наименование",max_length=255)
    qualification = models.CharField("Квалификация",max_length=255)
    class Meta:
        abstract = True


class GeneralFunction(WorkFunction):
    prof_standart = models.ForeignKey(ProfStandart, related_name='general_functions', on_delete=models.CASCADE)
    possible_jobs = models.JSONField()
    edu_requirements = models.JSONField()
    requirement_experience = models.JSONField()
    special_conditions = models.JSONField()


class ParticularFunction(WorkFunction):
    general_function = models.ForeignKey(GeneralFunction, related_name='particular_functions', on_delete=models.CASCADE)
    labor_act = models.JSONField()
    req_skill = models.JSONField()
    knowledge = models.JSONField()


