from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(request.POST)
        if user is not None:
            login(request, user)
            print('done')
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password')
            return render(request, 'Authentication/login.html')


    return render(request, 'Authentication/login.html')

def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong')
    return render(request, 'Authentication/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')
