from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from AppOne.models import Student
# Create your views here.

class StudentListView(ListView):
    model =  Student
#     By default_Template name is student_list.html
#     By Default context_object_name is student_list

class StudentDetailView(DetailView):
    model = Student
    #     By default_Template name is student_detail.html
    #     By Default context_object_name is student


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
#     By default_Template name is student_form.html
#     By Default context_object_name is student


