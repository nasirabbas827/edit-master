from django.contrib.auth.models import User
from django.db import models
from django.core import validators

from django.db import models
from django.contrib.auth.models import User
from django.core import validators

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    phone_number = models.CharField(
        max_length=20,
        default="",
        blank=True,
        null=True,
        validators=[validators.RegexValidator(regex='^[0-9]*$', message='Enter a valid phone number.', code='invalid_number')]
    )  # Only allow numeric values
    address = models.TextField(default="", blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')  # Add this line for profile picture

    def __str__(self):
        return self.user.username

# models.py
from django.db import models

class UploadedPDF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='uploaded_pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.pdf_file.name}'
