from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = True
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            return render(request, 'catalog/register_done.html')
    form = RegisterForm()
    return render(request, 'catalog/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            password = cd['password']
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return render(request, 'catalog/profile.html')
    form = LoginForm()
    return render(request, 'catalog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'catalog/logout.html')


# def ppppp(request):
#     print(request.user)
#     return render(request, 'ppppp.html')