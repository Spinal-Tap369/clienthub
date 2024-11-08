from .forms import UserProfileCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import group_required
from django.views.decorators.csrf import ensure_csrf_cookie
from home.models import Profile
from django.http import JsonResponse
from django.template.loader import render_to_string

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
    # Handle AJAX request for search
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_query = request.GET.get('query', '')
        profiles = Profile.objects.filter(user__username__icontains=search_query)
        html = render_to_string('partials/profile_list.html', {'profiles': profiles})
        return JsonResponse({'html': html})
    # all users to list all users!
    all_users = Profile.objects.all()
    context = {'form': form, 'page': 'Registration', 'profiles': all_users}  
    return render(request, 'register.html', context=context)
