from django.shortcuts import render,redirect
from AppOne.models import Employee
from AppOne.forms import EmployeeForm
# Create your views here.
def getemployee(request):
    var = Employee.objects.all()  # select * from Table_Name
    return render(request,'template/index.html',{'var':var})


def createemployee(request):
    var1 = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'template/create.html',{'var1':var1})


def deleteemployee(request,id):
    stu = Employee.objects.get(id=id)
    stu.delete()
    return redirect('/')

