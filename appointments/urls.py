from django.urls import path
from . import views

urlpatterns = [
path('', views.appointments_list, name='appointments_list'),
path('create/', views.appointment_form, name='appointment_form'),
path('<int:pk>/confirmation/', views.appointment_delete, name='appointment_delete'),
]