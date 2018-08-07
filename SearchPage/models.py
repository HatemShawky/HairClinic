
from django.db.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_14(value):
    if len(value) != 14:
        raise ValidationError(
            _('Should contain exactly 14 digits'),
            params={'value': value},
        )
    
def validate_nostr(value):
    if not value.isdigit():
        raise ValidationError(
            _('Should only contain digits'),
            params={'value': value},
        )
    
# Create your models here.
gender_choices=[('M','Male'),('F','Female')]
marital_choices=[('Single','Single'),("Married","Married"),("Divorced","Divorced"),("Widowed","Widowed")]
contrac_choice=[("None","None"),("IUD","IUD"),('Pills','Pills')]

class Patients(Model):
    name=CharField(max_length=30)
    clinicid=CharField(max_length=30,unique=True) #formatted as index of the patient admission in a certain month index-mm/yy : 4-07/18
    admdate=DateField(auto_now_add=True)
    age=IntegerField()
    gender=CharField(max_length=30,choices=gender_choices)
    marital=CharField(max_length=30,choices=marital_choices,blank=True)
    contrac=CharField(max_length=30,choices=contrac_choice,default='None')
    address=CharField(max_length=30,blank=True)
    occupation=CharField(max_length=30,blank=True)
    tel=CharField(blank=True,validators=[validate_nostr],unique=True,max_length=30)
    socialid=CharField(max_length=14,validators=[validate_14,validate_nostr],unique=True,blank=True)
    
    def __str__(self):
    
        return self.name
        