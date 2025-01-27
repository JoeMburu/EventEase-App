from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event
from django import forms

User = get_user_model()

class Booking(models.Model):
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # New field
    booking_date = models.DateTimeField(auto_now_add=True)    
    reminder = models.CharField(
        max_length=20,
        choices=[
            ('YES', 'Yes'),
            ('NO', 'No'),           
        ],
        default='NO'
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[            
            ('NOT_PAID', 'Not Paid'),
            ('PAID', 'Paid'),
            ('REFUNDED', 'Refunded'),
        ],
        default='NOT_PAID'
    )
    booking_status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('CONFIRMED', 'Confirmed'),            
            ('CANCELED', 'Canceled'),
            ('COMPLETED', 'Completed'),
        ],
        default='PENDING'
    )   

    class Meta:
        ordering = ['-booking_date']  # Latest bookings first
        unique_together = ('user', 'event')  # Prevent duplicate bookings for the same user-event pair

    def __str__(self):
        return f"{self.user.email} - {self.event.title} - {self.booking_status} - {self.payment_status}"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = []       
