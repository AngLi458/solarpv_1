from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'solarpv/index.html')

def register(request):
    return render(request, 'solarpv/register.html')

def login(request):
    return render(request, 'solarpv/login.html')

def webportal(request):
    return render(request, 'solarpv/webportal.html')
