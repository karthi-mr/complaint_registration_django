from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ? Register / Create User
class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Enter your username',
                                widget=forms.TextInput, error_messages={'required': "Username must not be empty."})
    password = forms.CharField(label='Enter your password', 
                               widget=forms.PasswordInput, error_messages={'required': "Password must not be empty."})