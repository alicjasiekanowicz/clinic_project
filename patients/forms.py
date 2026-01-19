from .models import Patient
from django import forms
from django.contrib.auth.models import User

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
        'name',
        'birthdate',
        'address',
        'phonenumber',
        'medicalhistory',
        'bloodtype'
]