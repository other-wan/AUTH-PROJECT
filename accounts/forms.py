
import imp
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
)


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'autocapitalize': 'none',
                'autocomplete': 'username',
                'placeholder': 'Username'
            })
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'autocomplete': 'new-password',
                'strip': False
            }
        )
    )

    def __init__(self, request: any = ..., *args: any, **kwargs: any) -> None:
        super().__init__(request, *args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
            self.fields[field].label = ""


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user: AbstractBaseUser, *args: any, **kwargs: any) -> None:
        super().__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
            self.fields[field].label = ""
