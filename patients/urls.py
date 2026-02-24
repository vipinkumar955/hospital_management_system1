from django.urls import path
from .views import patient_list,add_patient,delete_patient,patient_detail

urlpatterns = [
    path('',patient_list, name='patient_list'),
    path('add/', add_patient, name='add_patient'),
    path('delete/<int:id>/',delete_patient, name='delete_patient'),
    path('detail/<int:id>/',patient_detail, name='patient_detail'),
]
