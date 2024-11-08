from .forms import UserProfileCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import group_required
from django.views.decorators.csrf import ensure_csrf_cookie
from home.models import Profile

@group_required("Support Group")
@ensure_csrf_cookie
def register_user(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully.")
            return redirect('support_homepage')
    else:
        form = UserProfileCreationForm()
    all_users = Profile.objects.all()
    context = {'form': form, 'page': 'Registration', 'profiles': all_users}  
    return render(request, 'register.html', context=context)
