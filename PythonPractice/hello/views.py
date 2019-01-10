from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage

# Create your views here.

def home(request):
    return render(request, 'hello/home.html')

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )