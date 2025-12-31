from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    person = {
        "name":"najeer",
        "age":30,
        "place":"palakkad"
    }

    return render(request,'index.html',person)

def about(request):
    return render(request,'about.html')
    
def booking(request):
    return render(request,'booking.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
   return render(request,'department.html')