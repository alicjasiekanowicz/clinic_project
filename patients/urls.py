from django.urls import path
from . import views

urlpatterns = [
path('list', views.patients_list, name='patients_list'),
path('create', views.patient_form, name='patient_form'),
]