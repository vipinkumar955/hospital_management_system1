from django.shortcuts import render, redirect, get_object_or_404
from .models import Appoinment
from .forms import AppoinmentForm
from django.core.paginator import Paginator


#  List
def Appoinment_List(request):
    page_obj = Appoinment.objects.all().order_by('id')

  
    return render(request, 'Appoinments/Appoinment_List.html', {
        'page_obj': page_obj
    })


#  Add
def add_appoinment(request):
    if request.method == "POST":
        form = AppoinmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Appoinment_List')
        else:
            print(form.errors)
    else:
        form = AppoinmentForm()
       

    return render(request, 'Appoinments/add_appoinment.html', {'form': form})


#  Edit
def edit_appoinment(request, id):
    appoinment = get_object_or_404(Appoinment, id=id)

    if request.method == "POST":
        form = AppoinmentForm(request.POST, instance=appoinment)
        if form.is_valid():
            form.save()
            return redirect('Appoinment_List')
        else:
            print(form.errors) 
    else:
        form = AppoinmentForm(instance=appoinment)

    return render(request, 'Appoinments/add_appoinment.html', {'form': form})


#  Delete
def delete_appoinment(request, id):
    appoinment = get_object_or_404(Appoinment, id=id)
    appoinment.delete()
    return redirect('Appoinment_List')