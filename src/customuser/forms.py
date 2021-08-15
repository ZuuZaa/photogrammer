from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from customuser.models import CustomUser


class RegistrationForm(UserCreationForm):
    
    password1       = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2       = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())    
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1','password2')


class AccountAuthenticationForm(forms.ModelForm):
    password    = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
