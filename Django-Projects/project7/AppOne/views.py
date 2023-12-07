from django.shortcuts import render
from .import forms
# Create your views here.

def Registrationform(request):
    form = forms.Registration()
    return render(request,'registration.html',{'form':form})
