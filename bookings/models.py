from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event

User = get_user_model()

class Booking(models.Model):
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')    
   
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
            ('PAID', 'Paid'),
            ('REFUNDED', 'Refunded'),
        ],
        default='PAID'
    )
    booking_status = models.CharField(
        max_length=20,
        choices=[
            ('VALID', 'Valid'),
            ('CANCELED', 'Canceled'),
        ],
        default='VALID'
    )
    # Metadata
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-booking_date']  # Latest bookings first
        unique_together = ('user', 'event')  # Prevent duplicate bookings for the same user-event pair

    def __str__(self):
        return f"{self.user.username} - {self.event.name} ({self.status})"
