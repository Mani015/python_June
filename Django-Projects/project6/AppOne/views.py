from django.shortcuts import render
from AppOne.models import Student
# Create your views here.

def Student_Info(request):
    stu = Student.objects.all()
    return render(request,'student_info.html',{'info': stu})



