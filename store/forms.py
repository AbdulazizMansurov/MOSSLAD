from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control text-center',
                                   'placeholder': 'username',
                                   'style': 'margin: 0 auto; margin-bottom:20px; width: 400px'
                               }))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control text-center',
                                   'placeholder': 'password',
                                   'style': 'margin: 0 auto; margin-bottom:20px; width: 400px'
                               }))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text="Максимум 150 сиволов",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control text-center',
                                   'placeholder': 'Имя пользователя',
                                   'style': 'margin: 0 auto; margin-bottom:20px; width: 300px'
                               }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Пароль',
        'style': 'margin: 0 auto; margin-bottom:20px; width: 300px'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Подтверждение пароля',
        'style': 'margin: 0 auto; margin-bottom:20px; width: 300px'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Email',
        'style': 'margin: 0 auto; margin-bottom:20px; width: 300px'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')