from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='id_username2', max_length=100)
    password = forms.CharField(label='id_password2', max_length=100)


class RegisterForm(UserCreationForm):
    # username = forms.CharField(required=False)
    # email = forms.CharField(required=False)
    # invite_code_input = forms.CharField(required=False)
    # inviteCode = forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "invite_code_input", "inviteCode")

    def clean_invite_code_input(self):
        invite_code_input = self.cleaned_data.get("invite_code_input")
        user_invite_codes = list(InviteCode.objects.all().values_list('invite_code', flat=True))
        if invite_code_input not in user_invite_codes:
            raise forms.ValidationError('20位注册码不正确,请确认您有正确的注册码')
        return invite_code_input
