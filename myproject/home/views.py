from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Departments

def index(request):

    numbers = {
        'num1': [x for x in range(11)] ,
    } 
    return render(request,'index.html',numbers)

def about(request):
    return render(request,'about.html')
    
def booking(request):
    return render(request,'booking.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
   dict_dept={
       'dept':Departments.objects.all()
   }
   return render(request,'department.html')