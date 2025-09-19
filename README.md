# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py

from django.contrib import admin
from .models import car,carAdmin
admin.site.register(car,carAdmin)

models.py

from django.db import models
from django.contrib import admin
class car(models.Model):
    car_name=models.CharField()
    car_model=models.CharField(max_length=100)
    car_number=models.IntegerField()
    fuel_type=models.CharField()
    fc=models.IntegerField()

class carAdmin(admin.ModelAdmin):
    list_display=('car_name','car_model','car_number','fuel_type','fc')

~~~
## OUTPUT!
[alt text](<Screenshot 2025-09-19 125142.png>)

Include the screenshot of your admin page.


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
