
from django import forms

from .models import Appoinment
   
class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = '__all__'
