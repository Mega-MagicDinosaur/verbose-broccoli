from django import forms
from django.contrib import auth

from user.models import PrefixModel


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = self.cleaned_data
        #  error checking here
        return cd


class SignupForm1(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = self.cleaned_data
        password = cd.get('password')
        symbols = {'~', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ':', ',', '.', "'", '"'}
        if len(password) < 8:
            self.add_error('password', "password is too short")
        if not any(char in symbols for char in password):
            self.add_error('password', "password does not contain any special characters")
        if not any(char.isdigit() for char in password):
            self.add_error('password', "password does not contain any digit")
        if not any(char.isalpha() for char in password):
            self.add_error('password', "password does not contain any letter")

        return cd


class SignupForm2(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    username = forms.CharField()
    prefix = forms.ChoiceField(choices=('39', '39'))
    # prefix = forms.ModelChoiceField(queryset=PrefixModel.objects.all(), to_field_name='prefix')
    number = forms.IntegerField()
    linkedin_user = forms.URLField()
    company = forms.CharField()
    department = forms.ChoiceField(choices=[('1', 'abc')])
    job_title = forms.CharField()
    policy_agreement_check = forms.BooleanField()

    def clean(self):
        cd = self.cleaned_data
        #  error checking here
        return cd


class SignupForm3(forms.Form):
    type_of_code = forms.ChoiceField(choices=[('1', 'abc')])
    code = forms.IntegerField()
    address = forms.CharField()
    turnover = forms.ChoiceField(choices=[('1', 'abc')])
    employees = forms.IntegerField()
    products = forms.CharField()
    sectors = forms.CharField()
    BOM_position = forms.CharField()
    linkedin_company = forms.URLField()
    email_company = forms.EmailField()
    policy_agreement_check = forms.BooleanField()

    def clean(self):
        cd = self.cleaned_data
        #  error checking here
        return cd
