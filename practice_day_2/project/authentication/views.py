from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# User Registration view
def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Register Successfully!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.warning(request, 'User is not exists.')
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.warning(request, 'Incorrect Password')
            return redirect('login')
        else:
            login(request, user)
            messages.success(request, 'User Login Successfully!!!')
            return redirect('home')
    return render(request, 'login.html', {'form': AuthenticationForm})

def userLogout(request):
    logout(request)
    messages.success(request, 'User Logout Successfully!!!')
    return redirect('login')