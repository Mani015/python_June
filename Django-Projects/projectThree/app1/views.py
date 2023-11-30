# Urls module define a app level folder
# Road map
# 1)views
# 2) urls ---> define application level
# 3)urls----> project level


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Tech(request):
    return HttpResponse("<h2>To define urls page in app level</h2>")