from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email',]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pic','bio',]

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','profile']
