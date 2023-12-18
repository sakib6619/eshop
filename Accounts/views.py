from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:        
            form = AuthenticationForm()
        return render(request, 'Accounts/login.html',locals())
    else:
        return redirect('profile')

def signup(request):
    if not request.user.is_authenticated: 
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'User created successful...!!')
                return redirect('login')
        else:
            form = SignUpForm()
        return render(request, 'Accounts/signup.html', locals())
    else:
        return redirect('profile')

def user_profile(request):
   if request.user.is_authenticated:
        user = User.objects.filter()
        return render(request, 'Accounts/profile.html')
   else:
       return redirect('login')
def user_logout(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successful..!')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'Accounts/changePass.html', locals())
    else:
        return redirect('login')
    