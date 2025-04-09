from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    about = models.TextField(blank=True)
    job = models.CharField(max_length=150, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'about', 'job', 'profile_image']
        
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
