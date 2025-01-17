from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    # these are the fields
    title = models.CharField(max_length=100)
    description = models.CharField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    image = models.ImageField(upload_to='events/images/', blank=True, null=True)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_organiser')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

