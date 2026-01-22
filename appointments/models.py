from django.db import models
from doctors.models import Doctor
from patients.models import Patient


class Appointment(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name= 'appointments')
   patient = models.ForeignKey(Patient, on_delete = models.CASCADE, related_name= 'appointments')

   date = models.DateField()
   time = models.TimeField()
   title = models.CharField(max_length=150)
   reason = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f"Doctor: {self.doctor.name} Patient: {self.patient.name} Date: {self.date} Time:{self.time}"