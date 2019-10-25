from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import parse_qsl
from .models import Service

# Create your views here.
def index(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'myapp/index.html', { 'services': services })
    else:
        print('ร้องขอทำมะดา')
        services = Service.objects.all()
        print(services)
        return render(req, 'myapp/index.html', { 'services': services })

def profile(req):
    services = Service.objects.all()
    print(services)
    return render(req, 'myapp/profile.html',{ 'services': services })

def Home(req):
    return render(req, 'myapp/home.html')

def account(req):
    return render(req, 'myapp/account.html')
