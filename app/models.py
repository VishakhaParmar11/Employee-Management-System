from django.db import models

# Create your models here.

class employee(models.Model):
    emp_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    emp_dept = models.CharField(max_length=50)
    salary = models.IntegerField()
    photo = models.ImageField(upload_to="app/emp_img")
    
