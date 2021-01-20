from django.shortcuts import render
from django.http import HttpResponse
from templates import users
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import views as auth_views
from users.forms import SignupForm,UserForm
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import UserM

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

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update.html'
    model = UserM
    fields = ['title','picture','website']

    def get_object(self):
        return self.request.user.profile
    
    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:login',kwargs={'username':username})