from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = []
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
           
           
            
        