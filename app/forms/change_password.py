from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    new_password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    new_password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
