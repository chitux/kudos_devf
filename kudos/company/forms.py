from django import forms
from company.models import Company

class Signup(forms.ModelForm):
    class Meta:
        model = Company
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
        exclude = ['invitation_code']