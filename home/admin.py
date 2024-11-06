from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Team, Profile

admin.site.register(Team)
admin.site.register(Profile)