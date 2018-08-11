from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
######
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

######
def validate_nostr(value):
    if not value.isdigit() :
        raise ValidationError(
            _('%(value)s Contains non-digit characters'),
            params={'value': value},
        )
######    
class add_patient(forms.Form):
    name=forms.CharField(label="Patient's name: ",strip=True,required=True)
    gender=forms.ChoiceField(choices=gender_choices,required=True)
    age=forms.IntegerField(required=True)
    marital=forms.ChoiceField(choices=marital_choices,required=False)
    clinicid=forms.CharField(help_text="example : 2-07/18",label="Patient's Hairclinic-serial-number: ",required=False)
    tel=forms.CharField(label="Patient's phone number: ",required=False,validators=[validate_nostr], widget=forms.TextInput(attrs={'type':'number'}))    
    occupation=forms.CharField(label="Occupation: ",required=False)
    address=forms.CharField(label="Address: ",required=False)
    socialid=forms.CharField(max_length=14,min_length=14,label="Social ID (14digits from left to right): ",required=False, validators=[validate_nostr])#,widget=forms.TextInput(attrs={'type':'number'})
    contrac=forms.ChoiceField(choices=contrac_choice,required=False)

#####
class add_hairloss(forms.Form):
    symptoms=forms.CharField(widget=forms.Textarea,required=False,label="Symptoms: ")
    onset=forms.ChoiceField(choices=HL_onset,required=False,label="Onset: ")
    course=forms.ChoiceField(choices=HL_course,required=False,label="Course: ")
    duration=forms.IntegerField(label="Duration (months): ",required=False)
    distribution=forms.ChoiceField(choices=HL_dist,required=False,label="Distribution: ")
    scalp=forms.CharField(required=False,label="Scalp condition: ")
    hairpull=forms.ChoiceField(choices=HL_hairpull,required=False,label="Hair pull test: ",initial="None")
    
#####
class add_AAreata(forms.Form):
    Type=forms.ChoiceField(choices=AAreata_type,required=False,label="Type: ")
    sites=forms.MultipleChoiceField(widget  = forms.CheckboxSelectMultiple,choices=AAreata_sites,required=False,label="Sites affected: ")
    scalp=forms.CharField(required=False,label="Scalp condition: ",widget=forms.Textarea)
    AA=forms.MultipleChoiceField(widget  = forms.CheckboxSelectMultiple,choices=AAreata_autoimmune,initial="None",label="Associated autoimmune diseases: ")
    nails=forms.MultipleChoiceField(widget  = forms.CheckboxSelectMultiple,choices=AAreata_nails,initial="None",label="Nails affection: ")
    atopy=forms.MultipleChoiceField(widget  = forms.CheckboxSelectMultiple,choices=AAreata_atopy,initial="None",label="Associated Atopy: ")
    familyH=forms.BooleanField(initial=False,label="Family history of Alopecia Areata: ",required=False)
    familyAA=forms.MultipleChoiceField(widget  = forms.CheckboxSelectMultiple,choices=AAreata_autoimmune,initial="None",label="Family history of Autoimmune diseases: ")
    salt=forms.CharField(required=False,label="Salt score: ")
#####
class add_AAlopecia(forms.Form):
    pattern=forms.CharField(widget=forms.Textarea,label="Pattern: ",required=False)
    sinlair=forms.CharField(required=False,label="Sinlair's score: ")
    menstrual=forms.BooleanField(initial=False,label="Menstrual Irregularities: ",required=False)
    hirsutism=forms.BooleanField(initial=False,label="Hirsutism: ",required=False)
    Acne=forms.BooleanField(initial=False,label="Acne: ",required=False)
    familyH=forms.BooleanField(initial=False,label="Family history of Androgenic Alopecia: ",required=False)
    