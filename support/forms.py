from django import forms
from django.contrib.auth.models import User
from home.models import Profile, Team

class UserProfileCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, required=True, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=True, label="Team", widget=forms.Select(attrs={'class': 'form-control'}))
    mobile = forms.CharField(max_length=15, required=False, label="Mobile Number", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['username', 'password', 'email', 'team', 'mobile']

    def save(self, commit=True):  # Change `commit: True` to `commit=True`
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        profile = super().save(commit=False)
        profile.user = user  # Link the Profile to the new User
        profile.team = self.cleaned_data['team']
        profile.mobile = self.cleaned_data['mobile']
        if commit:
            profile.save()
        return profile
