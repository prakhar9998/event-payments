from django.forms import ModelForm
from django import forms
from paytm.models import PlayersInfo

class PlayersInfoForm(ModelForm):
    class Meta:
        model = PlayersInfo
        fields = [
            'leader_fullname',
            'contact_no',
            'member_1',
            'member_2',
            'member_3',
            'member_4',
        ]

        widgets = {
            'leader_fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp no.'}),
            'member_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PUBG Username'}),
            'member_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PUBG Username'}),
            'member_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PUBG Username'}),
            'member_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PUBG Username'})
        }