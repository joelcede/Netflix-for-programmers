from django.shortcuts import render
from django.http import HttpResponse
from templates import users
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from users.forms import SignupForm
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

# Create your views here.
"""
def initNetflix(request):
    return render(request, 'init.html')
"""

class InitNetflix(auth_views.LoginView):
    template_name = 'users/init.html'

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)