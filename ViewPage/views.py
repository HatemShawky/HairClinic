from django.shortcuts import render
from SearchPage.models import *

# Create your views here.
def view_patient(request,pkid):
    #selecting via pkid
    mymatch=Patients.objects.get(pk=pkid)
    print(mymatch)
    context={"patient":mymatch}
    return render(request,"view_patient.html",context)
    