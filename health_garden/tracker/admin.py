#register models

from django.contrib import admin
from .models import food, water, medication

@admin.register(food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'calories']

@admin.register(water)
class WaterAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')

@admin.register(medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency_type', 'days')