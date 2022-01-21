from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    now = datetime.datetime.now()
    html = "<html><body>Hello, It's now %s.</body></html>" % now
    return HttpResponse(html)

def contact_view(request, *args, **kwargs):
    html = "<html><body>Contact View</body></html>"
    return HttpResponse(html)
