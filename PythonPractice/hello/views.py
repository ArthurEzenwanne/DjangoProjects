from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')    

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )