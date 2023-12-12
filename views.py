# anomaly_app/views.py

from django.shortcuts import render, redirect
from .models import Anomaly
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

@login_required
def dashboard(request):
    anomalies = Anomaly.objects.all()
    return render(request, 'anomaly_app/dashboard.html', {'anomalies': anomalies})

def home(request):
    anomalies = Anomaly.objects.all()
    return render(request, 'anomaly_app/home.html', {'anomalies': anomalies})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'anomaly_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'anomaly_app/register.html', {'form': form})
