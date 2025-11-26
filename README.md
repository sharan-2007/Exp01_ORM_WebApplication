# Ex01 Django ORM Web Application
## Date: 26.11.2026

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=20, help_text="Enter Student Name")
    age = models.IntegerField(help_text="Enter age between 18 to 22")
    dob = models.DateField()
    reg_no = models.IntegerField(help_text="Enter the Register Number")

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'age', 'dob', 'reg_no']

admin.py
from django.contrib import admin
from .models import Student, StudentAdmin
# Register your models here.
admin.site.register(Student, StudentAdmin)
```
## OUTPUT
![alt text](<WhatsApp Image 2025-11-26 at 11.04.12_a6838348.jpg>)
![alt text](<WhatsApp Image 2025-11-26 at 11.04.12_ab7ab29d.jpg>)
![alt text](<WhatsApp Image 2025-11-26 at 11.04.12_03706bdc.jpg>)
## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
