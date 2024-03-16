from django.contrib import admin
from .models import OccupationGroup, EconomicActivity, Speciality
# Register your models here.

admin.site.register(OccupationGroup)
admin.site.register(EconomicActivity)
admin.site.register(Speciality)
