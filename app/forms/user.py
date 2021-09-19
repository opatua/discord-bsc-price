from django import forms
from django.contrib.auth.forms import UserCreationForm

from src.models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch'
            )
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.clean_password2())
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'is_active'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class UserPasswordChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('password',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'type': 'password', },
        )
