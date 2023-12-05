from django.contrib import admin
from AppOne.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Sname','Smarks','Sid']


admin.site.register(Student,StudentAdmin)
