import re
from django.shortcuts import render
from expr import models
from expr.models import Users
from expr.forms import UsersForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UsersForm(data = request.POST)
        # process form data
        if form.is_valid():
            obj = Users() #gets new object
            print()
            obj.fname = form.cleaned_data['fname']
            obj.lname = form.cleaned_data['lname']
            obj.phone = form.cleaned_data['phone']
            obj.email = form.cleaned_data['email']
            obj.password = form.cleaned_data['password']
            obj.save()
            return render(request, 'index.html')
    return render(request, 'signup.html')

def login(request):
    return render(request, 'index.html')
