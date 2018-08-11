
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
#Patientdata choices
gender_choices=[('M','Male'),('F','Female')]
marital_choices=[('Single','Single'),("Married","Married"),("Divorced","Divorced"),("Widowed","Widowed")]
contrac_choice=[("None","None"),("IUD","IUD"),('Pills','Pills')]
#Hairloss choices
HL_onset=[("gradual","gradual"),("sudden","sudden")]
HL_course=[("progressive","Progressive"),("regressive","Regressive"),("stationary","Stationary"),("RE","Remissions and Exacerbations")]
HL_dist=[("diffuse","Diffuse"),("frontal","Frontal"),('temporal',"Temporal"),("occipital","Occipital"),("vertical","Vertical")]
HL_hairpull=[("+ve","Positive"),("-ve","Negative"),("None","Not done")]
#AlopeciaAreata Choices
AAreata_type=[('S','Single patch'),('M','Multiple patches'),('AT','Alopecia Totalis'),('AU','Alopecia Universalis'),('D','Diffuse')]
AAreata_sites=[('Scalp',"Scalp"),('Beard',"Beard"),('EB',"Eyebrows"),('EL',"Eyelashes"),('Body',"Body")]
AAreata_autoimmune=[("None","None"),('T',"Thyroid"),("LE","Lupus Erythromatosis"),("DM","Diabetes Melitus"),
                    ("V","Vitiligo"),("IBD","Inflamatory Bowel Disease"),("ITP","Idiopathic Thrombocytopenia"),("RA","Rheumatoid Arthritis"),("PA","Pernicious Anemia")]#default is none
AAreata_nails=[("None","None"),("Pitting","Pitting"),("Brittle","Brittle"),("LR","Longitudinal ridging"),('Oncholysis',"Onycholysis"),("Onchomadesis","Onychomadesis")]
AAreata_atopy=[("None","None"),("AD","Atopic dermatitis"),("AR","Allergic rhinitis"),("HF","Hay fever")]


class Patients(Model):
    name=CharField(max_length=30)
    clinicid=CharField(max_length=30,unique=True) #formatted as index of the patient admission in a certain month index-mm/yy : 4-07/18
    admdate=DateField(auto_now_add=True)
    age=IntegerField(null=True)
    gender=CharField(max_length=30,choices=gender_choices)
    marital=CharField(max_length=30,choices=marital_choices,blank=True)
    contrac=CharField(max_length=30,choices=contrac_choice,default='None')
    address=CharField(max_length=30,blank=True)
    occupation=CharField(max_length=30,blank=True)
    tel=CharField(blank=True,validators=[validate_nostr],unique=True,max_length=30)
    socialid=CharField(max_length=14,validators=[validate_14,validate_nostr],unique=True,blank=True)
    
    def __str__(self):
    
        return self.name

class Hairloss(Model):
    patient=ForeignKey("Patients",on_delete=CASCADE,null=True)
    symptoms=TextField(blank=True)
    onset=CharField(max_length=30,choices=HL_onset,blank=True)
    course=CharField(max_length=30,choices=HL_course,blank=True)
    duration=IntegerField(blank=True)
    distribution=CharField(max_length=30,choices=HL_dist,blank=True)
    scalp=TextField(blank=True)
    hairpull=CharField(max_length=30,choices=HL_hairpull,default="None")
    
    def __str__(self):
        return self.patient.name
    
class AAreata(Model):#NB : CheckboxSelectMultiple will be used in the form not here , check  https://docs.djangoproject.com/en/2.1/ref/forms/widgets/#checkboxselectmultiple
    #and https://djangosnippets.org/snippets/1200/
    patient=ForeignKey("Patients",on_delete=CASCADE)
    Type=CharField(max_length=30,choices=AAreata_type,blank=True)
    sites=CharField(max_length=150,blank=True)
    AA=CharField(max_length=150,default='None')
    nails=CharField(max_length=150,default='None')
    atopy=CharField(max_length=150,default='None')
    familyH=BooleanField(default=None)
    familyAA=CharField(max_length=150,default='None')
    salt=CharField(max_length=30,blank=True)#ask about the format of this score
    
    def __str__(self):
        return self.patient.name
    
class AAlopecia(Model):
    patient=ForeignKey("Patients",on_delete=CASCADE)
    pattern=TextField(blank=True)
    sinlair=CharField(max_length=30,blank=True)#ask about the format of this score
    menstrual=BooleanField(default=None)
    hirsutism=BooleanField(default=None)
    acne=BooleanField(default=None)
    familyH=BooleanField(default=None)
    
    def __str__(self):
        return self.patient.name    