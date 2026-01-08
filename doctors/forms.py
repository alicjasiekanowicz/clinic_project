from .models import Doctor
from django import forms

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = "__all__"
        
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