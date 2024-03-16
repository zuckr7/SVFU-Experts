from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


spo = 0
bachalour = 1
master = 2
specialist = 3
EDU_LEVEL = ((spo, "Среденнее образование"), (bachalour, "Бакалавриат"), (master, "Магистратура"), (specialist,"Специалитет"))

russian = 0
english = 1
EDU_LANG = ((russian, "Русский"),(english, "Английский"))

class TrainingProgram(models.Model):
    number = models.CharField("Номер", max_length=10, db_index=True)
    name = models.CharField("Наименование", max_length=300, db_index=True)  # Название программы обучения
    brief_name = models.CharField("Краткое наименование", max_length=10)
    duration = models.IntegerField("Продолжительность", validators=[MinValueValidator(1), MaxValueValidator(6)])  # Продолжительность программы
    level = models.IntegerField("Уровень образования", choices=EDU_LEVEL)
    language = models.IntegerField("Язык обучения", choices=EDU_LANG)
    description = models.TextField("Описание")
    zet = models.IntegerField("ЗЕТ", validators=[MinValueValidator(1), MaxValueValidator(361)])
    

