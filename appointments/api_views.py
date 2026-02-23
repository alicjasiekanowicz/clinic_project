from django.http import JsonResponse

def appointments_api(request):
    data = []
    if hasattr(request.user, 'patient_profile'):
        appointments = request.user.patient_profile.appointments.select_related("doctor")
    elif hasattr(request.user, 'doctor_profile'):
        appointments = request.user.doctor_profile.appointments.select_related("patient")
    else:
        return JsonResponse({"error": "Unauthorized"}, status = 403)
    for appointment in appointments:
        data.append({ "id" : appointment.id, "date": str(appointment.date), "time": str(appointment.time),  "status": appointment.status,  "doctor": appointment.doctor.name,  "patient": appointment.patient.name  })
    return JsonResponse(data, status = 200, safe = False)
