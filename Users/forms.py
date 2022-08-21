from django import forms
from Users.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'role',
            'first_name',
            'last_name',
            'email',
            'pro_pic',
            'address',
            'line1',
            'city',
            'state',
            'pin_code',
            'username',
            'password1',
            'password2',
        ]


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
