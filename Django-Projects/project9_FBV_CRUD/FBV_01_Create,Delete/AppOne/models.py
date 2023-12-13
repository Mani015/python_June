from django.db import models

# Create your models here.

class Employee(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Salary = models.IntegerField()
    Domain = models.CharField(max_length=40)
    Experience = models.CharField(max_length=50)

