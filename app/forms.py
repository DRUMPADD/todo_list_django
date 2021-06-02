from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import Input

from .models import register

class signUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First name',
        }
    ))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last name',
        }
    ))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'User name',
        }
    ))
    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        }
    ))
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm password',
        }
    ))
    # lname = forms.CharField(max_length=200)
    class Meta:
        model = register
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

class PrettyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(PrettyAuthenticationForm, self).__init__(*args, **kwargs)
    username = forms.EmailField(widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'hi',
        }))