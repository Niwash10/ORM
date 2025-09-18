from django.db import models
from django.contrib import admin
class Movie(models.Model):
    car_name=models.CharField()
    car_model=models.CharField(max_length=100)
    car_number=models.IntegerField()
    fuel_type=models.CharField()
    fc=models.IntegerField()

class MovieAdmin(admin.ModelAdmin):
    list_display=('car_name','car_model','car_number','fuel_type','fc')

