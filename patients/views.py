from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm


# Patient List
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})
# Add Patient
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'patients/add_patient.html', {'form': form})


# Delete Patient
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('patient_list')


# Patient Detail (Without Medical History)
def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)

    return render(request, 'patients/patient_detail.html', {
        'patient': patient
    })