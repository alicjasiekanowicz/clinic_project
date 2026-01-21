from django.shortcuts import render,redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm 
from accounts.forms import RegisterForm
from django.contrib.auth.decorators import login_required


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

def patient_detail(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request,"patients/patient_detail.html",{ "patient": patient })

def patient_modify(request,pk):
    patient= get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient_form = PatientForm(request.POST,instance=patient)
        user_form = RegisterForm(request.POST,instance=request.user)
        if patient_form.is_valid() and user_form.is_valid() :
           patient_form.save()
           user_form.save()
        return redirect("patients_list")   
    else: 
        patient_form = PatientForm(instance=patient)
        user_form = RegisterForm(instance=request.user)
    return render(request, "patients/patient_form.html",{'user_form': user_form,'patient_form': patient_form})

@login_required
def patient_delete(request,pk):
    patient= get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect("patients_list")
    return render(request,"patients/patient_confirmation.html",{"patient":patient})

def patient_dashboard(request):
    pass
