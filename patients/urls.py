from django.urls import path
from . import views

urlpatterns = [
path('list', views.patients_list, name='patients_list'),
path('create', views.patient_form, name='patient_form'),
path('<int:pk>', views.patient_detail, name='patient_detail'),
path('<int:pk>/confirmation/', views.patient_delete, name='patient_confirmation'),
path('<int:pk>/modify/', views.patient_modify, name='patient_modify'),
]