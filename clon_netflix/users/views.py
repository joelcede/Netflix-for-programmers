from django.shortcuts import render
from django.http import HttpResponse
from templates import users
from django.views.generic import TemplateView

# Create your views here.
def base(request):
    return render(request,'base.html')

def inicial(request):
    return render(request, 'init.html')

def lg(request):
    return render(request, 'content_urlp/content_login.html')
