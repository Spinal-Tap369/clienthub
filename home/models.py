from django.db import models
from django.contrib.auth.models import User, Group

class Team(models.Model):
    name = models.CharField(max_length=100, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, related_name='teams')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_teams')

    def __str__(self) -> str:
        return f"{self.name} ({self.group.name})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='profile')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='team_members')
    mobile = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} ({self.team.name if self.team else 'No Team'})"