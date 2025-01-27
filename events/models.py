from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    # these are the fields
    title = models.CharField(max_length=100)
    description = models.CharField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255, blank=True, help_text="Webinar or physical location")
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")   
    image = CloudinaryField('image', default='placeholder')
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_organiser')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # New field
    
    def __str__(self):
        return self.title

