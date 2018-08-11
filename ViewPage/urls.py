from django.urls import path

from . import views
from . import models

urlpatterns = [
    path('<int:pkid>/',views.view_patient, name="view_patient"), #url customized for a patient's PK
    
]
