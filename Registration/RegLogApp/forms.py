from django import forms
from .models import OjasUserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "email")


class OjasUserProfileForm(forms.ModelForm):
    class Meta:
        model = OjasUserProfile
        fields = ("portfolio_site", "profile_pic")