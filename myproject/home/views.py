from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Departments,Doctors
from .forms import BookingForm
def index(request):

    numbers = {
        'num1': [x for x in range(11)] ,
    } 
    return render(request,'index.html',numbers)

def about(request):
    return render(request,'about.html')
    
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def doctors(request):
    dicts_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dicts_docs)

def contact(request):
    return render(request,'contact.html')

def department(request):
   if request.method == "POST":
       form =BookingForm(request.POST)
       if form.is_valid():
           form.save()
                    
   form = BookingForm()
   dict_dept={
       'dept':Departments.objects.all()
   }
   return render(request,'department.html',dict_dept)