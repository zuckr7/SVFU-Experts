from django.db import models

class TrainingProgram(models.Model):
    number = models.CharField("Номер", max_length=10, db_index=True)
    name = models.CharField("Наименование", max_length=300, db_index=True)  # Название программы обучения
    brief_name = models.CharField("Краткое наименование", max_length=10)
    duration = models.DurationField()  # Продолжительность программы
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)  # Преподаватель
    materials = models.ManyToManyField('Material')  # Материалы для обучения

class Instructor(models.Model):
    name = models.CharField("Имя", max_length=100)


class Material(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True, null=True)
