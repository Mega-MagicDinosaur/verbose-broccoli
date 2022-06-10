from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clear(self):
        cd = self.cleaned_data
        #  error checking here
        return cd


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clear(self):
        cd = self.cleaned_data
        #  error checking here
        return cd
