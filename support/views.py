from django.views.decorators.csrf import ensure_csrf_cookie
from .utils import group_required
from django.shortcuts import render

@group_required("Support Group")
@ensure_csrf_cookie
def register_user(request):
    print("Session key:", request.session.session_key)
    print("User authenticated in support view:", request.user.is_authenticated)
    context = {'page': 'Registration'}
    return render(request, 'register.html', context=context)
