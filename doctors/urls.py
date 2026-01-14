from django.urls import path
from . import views

urlpatterns = [
path('', views.doctors_list, name='doctors_list'),
path('create', views.doctor_form, name='doctor_form'),
path('<int:pk>', views.doctor_detail, name='doctor_detail'),
path('<int:pk>/modify/', views.doctor_modify, name='doctor_modify'),
path('<int:pk>/confirmation/', views.doctor_delete, name='doctor_confirmation'),
path('<int:pk>/dashboard/', views.doctors_dashboard, name='doctors_dashboard')
]