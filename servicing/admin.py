from django.contrib import admin

# Registering my models here.

from .models import Car

@admin.register(Car)
class carAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'car_notes', 'car_number', 'year_old']  