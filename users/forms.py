from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput, Select, Textarea, EmailInput, PasswordInput, TimeInput, NumberInput

from .models import CustomUser


# signup
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

        widgets = {

            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'phone_number': NumberInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['phone_number', 'password']
        exclude = ['username', 'first_name', 'last_name', 'email']

        widgets = {

            'phone_number': NumberInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': PasswordInput(attrs={'class': 'form-control'}),
        }


# class LoginForm(forms.ModelForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('phone_number', 'username')
#
#         widgets = {
#
#             'phone_number': NumberInput(attrs={'class': 'form-control'}),
#             'username': TextInput(attrs={'class': 'form-control'}),
#         }








