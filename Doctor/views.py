from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Bio, Schedule
from .forms import DoctorForm, BioForm, ScheduleForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Doctor/doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    form = DoctorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    else:
        print(form.errors) 
    return render(request, 'Doctor/doctor_form.html', {'form': form})
    
def update_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    form = DoctorForm(request.POST or None, request.FILES or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, 'Doctor/doctor_form.html', {'form': form})

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    doctor.delete()
    return redirect('doctor_list')

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    bio = Bio.objects.filter(doctor=doctor).first()
    schedules = Schedule.objects.filter(doctor=doctor)
    return render(request, 'Doctor/doctor_detail.html', {
        'doctor': doctor,
        'bio': bio,
        'schedules': schedules
    })

def add_bio(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    form = BioForm(request.POST or None)

    if form.is_valid():
        bio = form.save(commit=False)
        bio.doctor = doctor
        bio.save()
        return redirect('doctor_detail', doctor_id=doctor.id)

    return render(request, 'Doctor/bio_form.html', {'form': form, 'doctor': doctor})

def add_schedule(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    form = ScheduleForm(request.POST or None)

    if form.is_valid():
        schedule = form.save(commit=False)
        schedule.doctor = doctor
        schedule.save()
        return redirect('doctor_detail', doctor_id=doctor.id)

    return render(request, 'Doctor/schedule_form.html', {'form': form, 'doctor': doctor})