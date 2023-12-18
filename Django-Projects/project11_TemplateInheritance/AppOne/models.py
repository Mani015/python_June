from django.db import models
from django.urls import reverse
# Create your models here.

class Student(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=40)
    Email = models.CharField(max_length=50)
    Marks = models.IntegerField()

    def get_absolute_url(self):
        return reverse('stu',args={self.pk})

#     Either provide a url or define a get_a
# bsolute_url method on the Model.

