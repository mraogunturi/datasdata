from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    username = forms.CharField(max_length=100, help_text='username')
    password = forms.CharField(max_length=150, help_text='Password')
    confirmpassword = forms.CharField(max_length=150, help_text='Confirm Password')
