from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from backend.models import *
from django.db.models import Q
#from .forms import RegisterForm

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'solarpv/index.html', {'username': -1})

def register(request):
    if request.method == 'POST':
        #print(request.POST)
        client_id = int(request.POST.get('client'))
        client = Client.objects.get(pk=client_id)
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        middle_name = request.POST.get('middlename')
        last_name = request.POST.get('lastname')
        job_title = request.POST.get('jobtitle')
        prefix = request.POST.get('prefix')
        staff = request.POST.get('staff')
        email = request.POST.get('email')
        cellphone = request.POST.get('cellphone')
        officephone = request.POST.get('officephone')
        #print('client: ', client)
        #print('username: ', username)
        #print('first_name: ', first_name)
        #print('middle_name: ', middle_name)
        #print('last_name: ', last_name)
        #print('job_title: ', job_title)
        #print('prefix: ', prefix)
        #print('staff: ', staff)
        #print('email: ', email)
        #print('cellphone: ', cellphone)
        #print('officephone: ' , cellphone)
        u = User(client=client, user_id=username, first_name=first_name, middle_name=middle_name, last_name=last_name, job_title=job_title, email=email, office_phone=officephone, cell_phone=cellphone, prefix=prefix, is_staff=staff)
        u.save()
        return render(request, 'solarpv/login.html', {'login_state': 0})

    else:
        clients = Client.objects.all()
        users = User.objects.all()
        usernames = []
        for user in users:
            usernames.append(user.user_id)
        return render(request, 'solarpv/register.html', {'clients': clients, 'usernames': usernames})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(user_id=username)
        if len(user) == 0:
            login_state = -1
            return render(request, 'solarpv/login.html', {'login_state': login_state})
        else:
            return render(request, 'solarpv/index.html', {'username': username})

    else: 
        return render(request, 'solarpv/login.html', {'login_state': 0})

def webportal(request):
    return render(request, 'solarpv/webportal.html')
