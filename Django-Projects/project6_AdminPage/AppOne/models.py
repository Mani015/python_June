from django.db import models

# Create your models here.

class Student(models.Model):
    Sid = models.IntegerField()
    Sname = models.CharField(max_length=30)
    Smarks = models.IntegerField()
    Slocation = models.CharField(max_length=30)


# Create your models here.
# Create your models here.
#  The Model class typically provides methods for querying, creating, updating, and deleting data in the underlying database,
#  making it easier to perform these operations without having to write complex SQL queries manually.
