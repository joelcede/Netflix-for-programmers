from django.shortcuts import render
from django.http import HttpResponse
from templates import users
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# Create your views here.
"""
def initNetflix(request):
    return render(request, 'init.html')
"""

class InitNetflix(auth_views.LoginView):
    template_name = 'users/init.html'

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'