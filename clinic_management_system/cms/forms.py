from django.forms import ModelForm
from .models import patientdata
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class patientform(ModelForm):
    class Meta:
        model=patientdata
        fields = ['name', 'age','data']

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class CustomUserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Username')
    email = forms.EmailField(required=True, label='Email Address')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirm Password')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        user = User.objects.create_user(username=username, email=email, password=password)
        return user


