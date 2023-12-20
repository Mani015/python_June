from django.shortcuts import render
from django.http import HttpResponse
from AppOne.forms import Product
# HTTP (hyper text Transfer), http is a stateless protocol,if a protocol is a statelss
# it means the server doesn't maintain a continues Connection server
# because socket connection is alived  every time it destroys
# {HTTP is a short term memory loss}
#
# Scalability: There are no.of scability server different app ,different web server,
# they are not work on the same server
#
# session tracking:To maintain a state despite the stateles of HTTP
# ex:You are maintain a e cart application to main server management.
#
# waht is session?: A session can be defined two ways[login & logout]
# ex: facebook, instragram, Gmail,
# thhis apps going to everything happen this login & logout
#
# Track user intraction:
# suppose they are accesing the web site  from that till close your browser or
# leave that website is called user interaction
# ex: My book show tickets, e-commerce
#
# Cookies support:
# 1).request.session ---->set_test_cookie()
# 2).request.session ---->test_cookie_worked()
# 3).request.session ---->delete_test_cookie()



def Page1(request):
    request.session.set_test_cookie()   # To set a cookie on your browser
    return HttpResponse('<h1>Set A cookie</h1>')

def Page2(request):
    if request.session.test_cookie_worked():
        print('Cookies are enable on server console')
        request.session.delete_test_cookie()
    return HttpResponse('<h2>Delete cookie</h2>')


# set_cookie(key,value)
def PageCount(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count']) + 1
    else:
        count = 1
    response = render(request,'count.html',{'count':count})
    response.set_cookie('count',count)
    return response



def index(request):
    return render(request,'index.html')

def AddProduct(request):
    form = Product()
    response = render(request,'addproduct.html',{'form' : form})
    if request.method == 'POST':
        form = Product(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['name']
            Quantity = form.cleaned_data['quantity']
            response.set_cookie(Name,Quantity,60)
    return response


def DisplayProduct(request):

    return render(request,'displayproduct.html')
