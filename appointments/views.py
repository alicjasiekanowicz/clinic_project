from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def appointments_list(request):
    appointments = Appointment.objects.all()
    return render(request,"appointments/appointments_list.html",{ "appointments": appointments })

def appointment_form(request):
    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            if hasattr(request.user, 'patient_profile'):
                appointment.patient = request.user.patient_profile
                print(request.user.patient_profile) 
                appointment.save()
                return redirect("appointments_list") 
 
    else: 
        appointment_form = AppointmentForm()
    return render(request, "appointments/appointment_form.html",{'appointment_form': appointment_form})
