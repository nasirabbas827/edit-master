from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'email', 'date_of_birth', 'phone_number', 'address', 'profile_picture']

# forms.py
from django import forms

class UploadPDFForm(forms.Form):
    pdf_file = forms.FileField()
