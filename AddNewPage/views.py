from django.shortcuts import render
from collections import defaultdict
from . import forms
from SearchPage import models

# Create your views here.
def newptinputpage(request):
    form_addpt=forms.add_patient()
    form_hairloss=forms.add_hairloss()
    form_AAreata=forms.add_AAreata()
    form_AAlopecia=forms.add_AAlopecia()
    context = {"form_addpt":form_addpt,"form_hairloss":form_hairloss,"form_AAreata":form_AAreata,"form_AAlopecia":form_AAlopecia}
    return render(request, "add_new.html", context)

def insert(request):
    #allforms = forms.InputForm(request.POST)#not sure if the multiple forms will work here
    form_addpt=forms.add_patient(request.POST)
    form_hairloss=forms.add_hairloss(request.POST)
    form_AAreata=forms.add_AAreata(request.POST)
    form_AAlopecia=forms.add_AAlopecia(request.POST)    
    if form_addpt.is_valid() or form_AAlopecia.is_valid() or form_AAreata.is_valid() or form_hairloss.is_valid():
        #p1=engine.Pizza(form_.cleaned_data['Pizza1_r'],myform.cleaned_data['Pizza1_h'],myform.cleaned_data['Pizza1_p'])
        # but lets try to save time and effort , but no idea what i am doing
        cleaneddict_addpt,cleaneddict_aareata,cleaneddict_aalopecia,cleaneddict_hairloss={},{},{},{} # dict of field names and values
        print(form_AAlopecia.fields.keys())
        print(form_AAreata.fields.keys())
        print(form_addpt.fields.keys())
        print(form_hairloss.fields.keys())
        for field_name in form_addpt.fields:
            try:
                print(f"HEREE> field name :  {field_name} ,, type :{type(field_name)} cleaned_dict; {cleaneddict_addpt} ,, cleaned data : {form_addpt.cleaned_data}")
                cleaneddict_addpt.update({field_name:form_addpt.cleaned_data[field_name]})
            except:
                pass
        for field_name in form_AAlopecia.fields:
            try:
                cleaneddict_aalopecia[field_name]=form_addpt.cleaned_data[field_name]
            except:
                pass            
        for field_name in form_AAreata.fields:
            try:
                cleaneddict_aareata[field_name]=form_addpt.cleaned_data[field_name]
            except:
                pass                
        for field_name in form_hairloss.fields:
            try:
                cleaneddict_hairloss[field_name]=form_addpt.cleaned_data[field_name]  
            except:
                pass                
        #establish the patient first
        cursorPDATA=models.Patients(**cleaneddict_addpt)
        cursorPDATA.save()
        #now the foreign key before inserting and saving
        pt_id=cursorPDATA.pk # not sure if that would work , i am referencing the cursor not the model itself
        cleaneddict_aalopecia['patient'], cleaneddict_hairloss['patient'], cleaneddict_aareata['patient']=(pt_id,pt_id,pt_id)
        #now insert and save (and pray alot)
        cursorHAIRLOSS=models.Hairloss(**cleaneddict_hairloss)
        cursorAAREATA=models.AAreata(**cleaneddict_aareata)
        cursorAALOPECIA=models.AAlopecia(**cleaneddict_aalopecia)
        cursorAALOPECIA.save(), cursorAAREATA.save(), cursorHAIRLOSS.save()
    else:
        print("not valid ?!?!")
    context={"Patient":cursorPDATA}
    return render(request,"success.html",context)
"""
read these : https://stackoverflow.com/questions/866272/how-can-i-build-multiple-submit-buttons-django-form
https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django
and edit the forms html file
"""