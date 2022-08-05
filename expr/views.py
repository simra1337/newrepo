import re
from django.shortcuts import render, HttpResponse
from expr import models
from expr.models import Users
from expr.forms import UsersForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        data = request.POST
        error_message = ""
        # process form data
        if form.is_valid():
            if data.get('cpassword')!=form.cleaned_data.get('password'):
                error_message = "Passwords do not match"
                return render(request, 'signup.html', {'error' : error_message, 'form': form})
            else:
                post = form.save(commit = False)
                post.save() 
                return HttpResponse("data submitted successfully")
        else:
            return render(request, "signup.html", {'form':form}) 
    else:
        form = UsersForm(None)
        return render(request, 'signup.html', {'form':form})

def login(request):
    return render(request, 'index.html')
