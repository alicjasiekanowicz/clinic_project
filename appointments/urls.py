from django.urls import path
from . import views, api_views

urlpatterns = [
path('', views.appointments_list, name='appointments_list'),
path('create/', views.appointment_form, name='appointment_form'),
path('<int:pk>/confirmation/', views.appointment_delete, name='appointment_delete'),
path('<int:pk>/approve/', views.approve_appointment, name="approve_appointment"),
path('<int:pk>/cancel/', views.cancel_appointment, name="cancel_appointment"),
path('api/list/', api_views.appointments_api, name='appointments_list'),
]