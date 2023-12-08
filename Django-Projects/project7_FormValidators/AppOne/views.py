from django.shortcuts import render
from .import forms
# Create your views here.

def Applicationform(request):
    f1 = forms.Application()
    if request.method == 'POST':
        form = forms.Application(request.POST)  # request.POST : taken all income user details
        if form.is_valid():
            print('Form is valid')
            print('ID :',form.cleaned_data['Id'])
            print('Firstname :', form.cleaned_data['Firstname'])
            print('Lastname :', form.cleaned_data['Lastname'])
            print('Mobilenumber :', form.cleaned_data['Mobile_No'])
            print('Email :', form.cleaned_data['Email'])
    return render(request,'template/Application.html',{'form':f1})




# Cleaned_data is an object, not a function. From the Django docs: A Form instance has an is_valid() method,
# which runs validation routines for all its fields.
# When this method is called, if all fields contain valid data, it will: return True.