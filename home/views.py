from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .utils import get_redirect_url_for_user

def index(request):
    return redirect('login/')

def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Ensures the user is logged in
                request.session['just_logged_in'] = True
                print("User is logged in:", request.user.is_authenticated)  # Debugging
                print("User groups after login:", request.user.groups.all())  # Debugging
                return get_redirect_url_for_user(user)
            else:
                form.add_error(None, 'Invalid credentials!')
    context = {'page': 'Login', 'form': form}
    return render(request, 'login.html', context=context)

def client_homepage(request):
    context = {'page': 'Client Side'}
    return render(request, 'client_homepage.html', context=context)

def support_homepage(request):
    print(request.user.groups.all())
    context = {'page': 'Support Side'}
    return render(request, 'support_homepage.html', context=context)

def default_homepage(request):
    context = {'page': 'default',}
    return render(request, 'default_homepage.html', context=context)
