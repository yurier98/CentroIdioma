from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget = widgets.TextInput(
#             attrs={'placeholder': "username", "class": "form-control"})
#         self.fields['password'].widget = widgets.PasswordInput(
#             attrs={'placeholder': "password", "class": "form-control"})



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "usuario",
                "value"       : "admin",
                "class"       : "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "contraseña",
                "value"       : "admin",
                "class"       : "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "usuario",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "correo",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "contraseña",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "contraseña",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
