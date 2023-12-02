from django.shortcuts import render

# Create your views here.

def Product1(request):
    dict1 = {
        'Product_Name': 'D-mart',
        'Product_Color': 'Green',
        "Product_price": 1000
    }
    return render(request,'intro.html',dict1)


def Product2(request):
    dict1 = {
        'Product_Name': 'D-mart',
        'Product_Color': 'Green',
        "Product_price": 1000
    }
    return render(request,'intro.html',dict1)
def Product3(request):
    dict1 = {
        'Product_Name': 'D-mart',
        'Product_Color': 'Green',
        "Product_price": 1000
    }
    return render(request,'intro.html',dict1)

def Product4(request):
    dict1 = {
        'Product_Name': 'D-mart',
        'Product_Color': 'Green',
        "Product_price": 1000
    }
    return render(request,'intro.html',dict1)


def index(request):
    return render(request,'index.html')
