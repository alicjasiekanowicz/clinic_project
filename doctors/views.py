from django.shortcuts import render,redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request,"doctors/doctors_list.html",{ "doctors": doctors })
@login_required
def doctor_form(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctors_list")  
    else: 
        form = DoctorForm()
    return render(request, "doctors/doctor_form.html", {"form": form})

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