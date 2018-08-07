from django.shortcuts import render

# Create your views here.
def view_patient(request,pkid):
    context={}
    return render(".html",context)
    