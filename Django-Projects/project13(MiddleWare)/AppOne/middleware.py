
from django.http import HttpResponse
class SimpleMiddleware:
    print('INIT Method')
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print('Init method Taken the Get_response')

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('Before The view is excuted')
        response = self.get_response(request)
        print('After The view is excuted')
        # Code to be executed for each request/response after
        # the view is called.
        return response

class ExceptionHandlingMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self,request,exception):
        print(exception.__class__.__name__)
        print(exception)
        return HttpResponse('<h4>We are currently facing the issues, please check the back in Few Minutes</h4>')