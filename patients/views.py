from django.shortcuts import render,redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm 
from accounts.forms import RegisterForm


def patients_list(request):
    patients = Patient.objects.all()
    return render(request,"patients/patients_list.html",{ "patients": patients })

def patient_form(request):
    if request.method == "POST":
        patient_form = PatientForm(request.POST)
        user_form = RegisterForm(request.POST)
        if patient_form.is_valid() and user_form.is_valid() :
            user = user_form.save(commit=False)
            user.save()
            patient_profile = patient_form.save(commit=False)
            patient_profile.user = user
            patient_profile.save()
            return redirect("patient_dashboard")   
    else: 
        patient_form = PatientForm()
    
        user_form = RegisterForm()
    return render(request, "patients/patient_form.html",{'user_form': user_form,'patient_form': patient_form})
