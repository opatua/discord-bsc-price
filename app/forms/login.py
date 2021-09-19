from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        ),
        required=True
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        ),
        required=True
    )