from django.shortcuts import render
from django.db.models import Q

from . import forms, models

# Create your views here.
def searchpage(request):
    context={ 'formhere1':forms.searchform() }
    return render(request, "searchpage.html", context)

def results(request):
    sfr=forms.searchform(request.POST) #search form results
    if sfr.is_valid():
        datadict={} #a dict will contain the search criterea needed (not left blank)
        pt_name=sfr.cleaned_data['pt_name']
        if pt_name != "":
            datadict["name"]=pt_name
        pt_phone=sfr.cleaned_data['pt_phone']
        if pt_phone != "":
            datadict["tel"]=pt_phone
        pt_hosp=sfr.cleaned_data['pt_hosp']
        if pt_hosp != "":
            datadict["clinicid"]=pt_hosp
        pt_socialid=sfr.cleaned_data['pt_socialid']
        if pt_socialid != "":
            datadict["socialid"]=pt_socialid
        #datadict={"name":pt_name,"clinicid":pt_hosp,"tel":pt_phone,"socialid":pt_socialid}
        result_pt=models.Patients.objects.filter(**datadict)
        if models.Patients.objects.filter(**datadict).count()>0:
            status="Found a match"
        else:
            status="Could't find a match"
            #result_pt=[]   

    context={"status":status,"results":result_pt}
    return render(request,"results.html",context)
    