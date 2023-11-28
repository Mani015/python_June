from django.http import HttpResponse
import datetime
def Current_DT(request):
    var = datetime.datetime.now()
    New = "<h1>Current Date & Time:</h1>" + str(var)
    return HttpResponse(New)
