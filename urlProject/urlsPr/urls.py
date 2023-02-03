from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
     path('',views.index,name="index"),
     path('createshorturl',views.createshorturl,name="createshorturl"),
     path("Result",views.Result,name="Result"), 
     re_path(r'^(?P<requested_url>.*)$', views.redirect_to_external_site),
]