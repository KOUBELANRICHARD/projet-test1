# zugus/forms.py

from django import forms
from zugus.models import Compte

class CreateAccountForm(forms.ModelForm):
    username = forms.CharField(max_length=25)  
    name = forms.CharField(required=False)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput) 

    class Meta:
        model = Compte
        fields = ['username', 'name', 'email', 'phone', 'password'] 

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)