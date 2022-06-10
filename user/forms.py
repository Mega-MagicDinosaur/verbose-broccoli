from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = self.cleaned_data
        #  error checking here
        return cd


class SignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    policy_agreement_check = forms.BooleanField()

    name = forms.CharField()
    surname = forms.CharField()
    username = forms.CharField()
    prefix = forms.ChoiceField(choices=[('1', 'abc')])
    number = forms.IntegerField()
    linkedin_user = forms.URLField()
    company = forms.CharField()
    department = forms.ChoiceField(choices=[('1', 'abc')])
    job_title = forms.CharField()

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

    def clean(self):
        cd = self.cleaned_data
        #  error checking here
        return cd
