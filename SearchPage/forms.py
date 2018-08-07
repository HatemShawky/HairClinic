from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_nostr(value):
    if not value.isdigit() :
        raise ValidationError(
            _('%(value)s Contains non-digit characters'),
            params={'value': value},
        )


class searchform(forms.Form):
    pt_name=forms.CharField(label="Patient's name: ",required=False)
    pt_phone=forms.CharField(label="Patient's phone number: ",required=False,validators=[validate_nostr], widget=forms.TextInput(attrs={'type':'number'}))    
    pt_hosp=forms.CharField(help_text="example : 2-07/18",label="Patient's Hairclinic-serial-number: ",required=False)
    pt_socialid=forms.CharField(max_length=14,min_length=14,label="Social ID (14digits from left to right): ",required=False, validators=[validate_nostr])#,widget=forms.TextInput(attrs={'type':'number'})
    
   
       