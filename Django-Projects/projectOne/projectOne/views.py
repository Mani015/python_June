# In views Always have to write down two types of objects:

# 1)FBV ---> Function Based Views
# 2)CBV ---> Class Based Views

# ROad Map:
# 1).Views
# 2).urls
# 3). runserver

from django.http import HttpResponse
def Student(request):
    return HttpResponse('<h1>Hello Student Good Moring!</h1>')
