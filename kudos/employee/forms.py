from django import forms
from employee.models import Employee, Kudo


class Signup(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['kudollars', 'company_id']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Write your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@exaple.com'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '10 digits please'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': '****************'
            }),
        }


class KudoForm(forms.ModelForm):
    class Meta:
        model = Kudo
        exclude = ['is_active']
        widgets = {
            'kudo_body': forms.Textarea(attrs={'rows': 4})
        }