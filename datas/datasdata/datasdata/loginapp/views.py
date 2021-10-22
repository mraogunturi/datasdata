from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .serializers import SignupSerializer
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'home.html')


def signup(request):
    # if request.method == 'post:
    form = SignupForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data('password')
        confirmpassword = form.cleaned_data('confirmpassword')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'loginapp/signup.html', {'form': form})


def login(request):
    return render(request,'loginapp/login.html')


def logout():
    pass


def reset():
    pass