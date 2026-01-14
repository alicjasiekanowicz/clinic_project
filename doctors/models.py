from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
   user = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name='doctor_profile'
   )
   name = models.CharField(max_length=100)
   years_of_experience = models.IntegerField()
   speciality = models.CharField(max_length=100)
   bio = models.TextField()
   def __str__(self):
      return f"Dr. {self.user.last_name} - {self.speciality}"
