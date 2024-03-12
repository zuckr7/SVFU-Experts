from django.db.models import Model, CharField, IntegerField

# Create your models here.
class TrainingProgram(Model):
    number = CharField("Номер", max_length=10, db_index=True)
    name = CharField("Наименование", max_length=300, db_index=True)  # Название программы обучения
    brief_name = CharField("Краткое наименование", max_length=10)
    duration = duration  # Продолжительность программы
    instructor = instructor  # Преподаватель
    materials = materials  # Материалы для обучения


