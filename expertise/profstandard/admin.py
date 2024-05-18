from django.contrib import admin
from .models import ProfStandart, GeneralFunction, ParticularFunction
# Register your models here.

admin.site.register(ProfStandart)
admin.site.register(GeneralFunction)
admin.site.register(ParticularFunction)