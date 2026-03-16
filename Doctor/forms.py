from django import forms
from .models import Doctor, Schedule

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day', 'start_time', 'end_time']
