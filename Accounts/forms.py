from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'id':'username',
            'placeholder':'Enter Username',
        })
        self.fields['email'].widget.attrs.update({
            'id':'email-id',
            'placeholder':'Email address...',
        })
        self.fields['password1'].widget.attrs.update({
            'id':'userpass',
            'placeholder':'Enter password...',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder':'Confirm password...',
        })
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']