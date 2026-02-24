from django.urls import path
from .views import *

urlpatterns = [
    path('', Appoinment_List, name='Appoinment_List'),
    path('add/', add_appoinment, name='add_appoinment'),
    path('edit/<int:id>/', edit_appoinment, name='edit_appoinment'),
    path('delete/<int:id>/', delete_appoinment, name='delete_appoinment'),
]