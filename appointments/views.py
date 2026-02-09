from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

def appointments_list(request):
    appointments = Appointment.objects.all()
    isPatient = False
    isDoctor = False
    if hasattr(request.user, 'patient_profile'):
        isPatient = True
    if hasattr(request.user, 'doctor_profile'):
        isDoctor = True
    return render(request,"appointments/appointments_list.html",{ "appointments": appointments, "isPatient" : isPatient, "isDoctor":isDoctor })

def appointment_form(request):
    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            isPatient = False
            isDoctor = False
            if hasattr(request.user, 'patient_profile'):
                appointment.patient = request.user.patient_profile
                isPatient = True
                print(request.user.patient_profile) 
                appointment.save()
                return redirect("appointments_list") 
            if hasattr(request.user, 'doctor_profile'):
                isDoctor = True
 
    else: 
        appointment_form = AppointmentForm()
        isPatient = False
        isDoctor = False
        if hasattr(request.user, 'patient_profile'):
            isPatient = True
        if hasattr(request.user, 'doctor_profile'):
            isDoctor = True
    return render(request, "appointments/appointment_form.html",{"appointment_form": appointment_form, "isPatient" : isPatient, "isDoctor":isDoctor})

def appointment_delete(request,pk):
    appointment= get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        appointment.delete()
        return redirect("appointments_list")
    return render(request,"appointments/appointment_confirmation.html",{"appointment":appointment})

@login_required
def approve_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if not hasattr(request.user, "doctor_profile"):
        print("You should be a doctor to perform this action...")
        return redirect("appointments_list")
    
    if appointment.doctor != request.user.doctor_profile:
        print("You're not the authorized doctor to perform this action...")
        return redirect("appointments_list")
    
    appointment.status = "approved"
    appointment.save()
    return redirect("appointments_list")

@login_required
def cancel_appointment(request, pk):
    pass