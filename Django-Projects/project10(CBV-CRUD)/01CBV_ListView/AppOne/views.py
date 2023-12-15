from django.shortcuts import render
from django.views.generic import ListView
from AppOne.models import Student
# Create your views here.

class StudentListView(ListView):
    model =  Student
#     By default_Template name is student_list.html
#     By Default context_object_name is student_list



