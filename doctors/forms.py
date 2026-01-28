from .models import Doctor
from django import forms
from django.contrib.auth.models import User
from accounts.forms  import RegisterForm

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
        'name',
        'speciality',
        'years_of_experience',
        'bio'

]

'''class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']'''



        
''' # Customize how fields look in
        widgets = {
        'name': forms.TextInput(attrs={
        'class': 'form-control', # CSS class
        'placeholder': 'Enter post name'
        }),
        'content': forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write your post here...',
        'rows': 5 # Height of text box
        }),
        }'''