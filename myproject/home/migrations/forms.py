from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        models = Booking
        Fields = '__all__'