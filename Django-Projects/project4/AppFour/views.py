from django.shortcuts import render

# Create your views here.
def Employee(request):
    return render(request,'basic.html')
    #render(request,'html file,context = variablename)

