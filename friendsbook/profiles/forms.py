# from django.contrib.auth import forms
from .models import Profile
from django import forms

# this is a modelform
class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'avatar']