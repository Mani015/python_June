from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from AppOne.models import Student
from django.urls import reverse_lazy
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


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student')
#     By default_Template name is student_confirm_delete.html
#     By Default context_object_name is student





