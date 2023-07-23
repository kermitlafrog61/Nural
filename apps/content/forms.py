from django import forms
from .models import UserContactInfo

class UserFooterForm(forms.ModelForm):
    class Meta:
        model = UserContactInfo
        fields = ['phone', 'instagram', 'facebook', 'telegram']
