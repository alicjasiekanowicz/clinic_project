from .models import Appointment
from django import forms

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
        'doctor',
        'date',
        'time',
        'title', 
        'reason',
        ]

        widget=forms.DateInput(
        attrs={
        'type': 'date',
        'class': 'form-control'
        }
        )