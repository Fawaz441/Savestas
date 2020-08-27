from django import forms
from django.forms import ValidationError

class SignupForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

    def clean_password(self):
        if self.cleaned_data.get('password') == self.cleaned_data.get('confirm_password'):
            raise ValidationError("Passwords must be the same!")