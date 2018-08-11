from django.urls import path

from . import views

urlpatterns = [
    path('',views.newptinputpage, name="input_new_page"),
    path('success/', views.insert, name='insert_successfull_page'),
]
