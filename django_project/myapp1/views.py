from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def home1(request):
    return render(request,'home1.html')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/myapp1/login/')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'a':form})

def login1(request):
    return render(request,'login.html')
