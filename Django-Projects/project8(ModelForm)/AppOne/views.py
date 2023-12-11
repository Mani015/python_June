from django.shortcuts import render
from AppOne  import forms
# Create your views here.

def Customer_Data(request):
    form = forms.Customer()
    if request.method == 'POST':
        form = forms.Customer(request.POST)
        if form.is_valid():
            print('Form is Success')
            print('Firstname = ',form.cleaned_data['Firstname'])
            print('Lastname = ', form.cleaned_data['Lastname'])
            print('Age = ', form.cleaned_data['Age'])
    return render(request,'template/Application.html',{'form':form})




# Cleaned_data is an object, not a function. From the Django docs: A Form instance has an is_valid() method,
# which runs validation routines for all its fields.
# When this method is called, if all fields contain valid data, it will: return True.