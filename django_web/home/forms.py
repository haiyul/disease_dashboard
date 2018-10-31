from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class RegisterForm(UserCreationForm):
    invite_code = forms.CharField(label='invite_code', max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
