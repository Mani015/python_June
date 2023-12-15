from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class Student(View):
    def get(self,request):
        return HttpResponse('<p>Hello student welcome to Class based views(CBV)</p>')