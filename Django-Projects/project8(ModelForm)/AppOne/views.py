from django.shortcuts import render
from AppOne.models import Product
from AppOne.forms import ProductForm
# Create your views here.


def index(request):
    return render(request,'index.html')


def productlist(request):
    var = Product.objects.all()  # select * from table_name
    return render(request,'listproduct.html',{'var':var})



def Addproduct(request):
    var1 = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)  #request.POST: It will submit data posted in HTML form elements.
        if form.is_valid():  #is_valid(): This function validates the form data against model field types and options.
            form.save()   # save(): This function saves the data in the database.
        return index(request)
    return render(request,'addproject.html',{'var1':var1})