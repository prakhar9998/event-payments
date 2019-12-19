from django.forms import ModelForm
from django import forms
from paytm.models import PersonInfo

class PersonInfoForm(ModelForm):
    class Meta:
        model = PersonInfo
        fields = [
            'full_name',
            'contact_no',
            'amount',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }