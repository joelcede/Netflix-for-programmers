from django import forms
from django.contrib.auth.models import User
from users.models import UserM as userModels

class SignupForm(forms.Form):
    username = forms.CharField(min_length=5,max_length=30)
    email = forms.CharField(min_length=6,max_length=70,widget=forms.EmailInput())
    password = forms.CharField(max_length=30,widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=30,widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=3,max_length=50)
    last_name = forms.CharField(min_length=3,max_length=50)

    def clean_username(self):
        username = self.cleaned_data['username']
        username_token = User.objects.filter(username=username).exists()
        if username_token:
            raise forms.ValidationError('Username in use')
        return username
    
    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('passwords are not the same')
        return data
    
    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = userModels(user=user)
        profile.save()

class UserForm(forms.Form):
    title = forms.CharField(max_length=60,required=True)
    picture = forms.ImageField()
    website = forms.URLField(max_length=200,required=True)
    description = forms.CharField(max_length=400,required=False)
    phone_number = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(max_length=40,required=False)