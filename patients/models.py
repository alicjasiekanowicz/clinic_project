from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
   user = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name='patient_profile'
   )
   name = models.CharField(max_length=100)
   birthdate = models.DateField()
   address = models.TextField()
   phonenumber = models.CharField(max_length= 15)
   medicalhistory = models.TextField()
   bloodtype = models.CharField(choices = [
    ('A+', 'A Positive'),
    ('A-', 'A Negative'),
    ('B+', 'B Positive'),  
    ('B-', 'B Negative'),
    ('AB+', 'AB Positive'),
    ('AB-', 'AB Negative'),
    ('O+', 'O Positive'),
    ('O-', 'O Negative')
    ])

   
   def __str__(self):
      return f"Patient {self.user.last_name}"
