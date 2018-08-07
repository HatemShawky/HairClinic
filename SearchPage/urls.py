from django.urls import path

from . import views

urlpatterns = [
    path('',views.searchpage, name="display_search_page"),
    path('results/',views.results, name="search_results"),
    
]
