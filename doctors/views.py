from django.shortcuts import render,redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm #UserRegistrationForm
from accounts.forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request,"doctors/doctors_list.html",{ "doctors": doctors })

#@login_required
def doctor_form(request):
    if request.method == "POST":
        doctor_form = DoctorForm(request.POST)
        user_form = RegisterForm(request.POST)
        if doctor_form.is_valid() and user_form.is_valid() :
            user = user_form.save(commit=False)
            user.save()
            doctor_profile = doctor_form.save(commit=False)
            doctor_profile.user = user
            doctor_profile.save()
            return redirect("doctors_dashboard")   
    else: 
        doctor_form = DoctorForm()
    
        user_form = RegisterForm()
    return render(request, "doctors/doctor_form.html",{'user_form': user_form,'doctor_form': doctor_form})

def doctor_detail(request,pk):
   doctor = get_object_or_404(Doctor, pk=pk)
   return render(request,"doctors/doctor_detail.html",{"doctor":doctor})
@login_required
def doctor_modify(request,pk):
    doctor= get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save() #saves record to the database
            return redirect("doctors_list")
    else:
        form = DoctorForm(instance=doctor) 
    return render(request,"doctors/doctor_form.html",{"form":form})
@login_required
def doctor_delete(request,pk):
    doctor= get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect("doctors_list")
    return render(request,"doctors/doctor_confirmation.html",{"doctor":doctor})

def doctors_dashboard(request, pk):
    doctor= get_object_or_404(Doctor, pk=pk)
    return redirect("doctors_dashboard") 