from django import forms
from company.models import Company

class Signup(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['invitation_code']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your company\'s name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Put your email here'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '10 digits please'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': '****************'
            }),
        }


class Login(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Company\'s email'}),
            'password': forms.PasswordInput(attrs={'placeholder': '*********'}),
        }