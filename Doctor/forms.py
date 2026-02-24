from django import forms
from .models import Doctor, Schedule, Bio

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day', 'start_time', 'end_time']

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['bio_text']