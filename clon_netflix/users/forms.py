from django import forms
from django.contrib.auth.models import User
from users.models import User as userModels

class SignupForm(forms.Form):
    username = forms.CharField(min_length=5,max_length=30)
    email = forms.CharField(
                            min_length=6,
                            max_length=70,
                            widget=forms.EmailInput()
                        )
    password = forms.CharField(
                                min_length=5,
                                max_length=30,
                                widget=forms.PasswordInput()
                            )
    password_confirmation = forms.CharField(
                                min_length=5,
                                max_length=30,
                                widget=forms.PasswordInput()
                            )
    first_name = forms.CharField(min_length=3,max_length=50)
    last_name = forms.CharField(min_length=3,max_length=50)

    def cleanUsername(self):
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