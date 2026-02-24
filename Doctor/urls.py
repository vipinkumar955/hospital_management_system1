from django.urls import path
from .views import add_bio, add_schedule, doctor_list, doctor_detail, add_doctor, update_doctor, delete_doctor

urlpatterns = [
    path('', doctor_list, name='doctor_list'),
    path('<int:doctor_id>/', doctor_detail, name='doctor_detail'),
    path('add/', add_doctor, name='add_doctor'),
    path('update/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('delete/<int:doctor_id>/', delete_doctor, name='delete_doctor'),
    path('<int:doctor_id>/schedule/add/', add_schedule, name='add_schedule'),
      path('<int:doctor_id>/bio/add/', add_bio, name='add_bio'),

]