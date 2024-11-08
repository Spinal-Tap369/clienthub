from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login_user'),
    path('client_homepage/', client_homepage, name='client_homepage'),
    path('support_homepage/', support_homepage, name='support_homepage'),
    path('logout/', LogoutView.as_view(), name='logout_user')
]