from django.db import models

# Create your models here.

class Product(models.Model):
    productname = models.CharField(max_length=30)
    productprice = models.IntegerField()
    productMFD = models.DateField()
    productEPD = models.DateField()

