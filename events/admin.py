from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'category', 'organiser', 'created_at')
    list_filter = ('category', 'date', 'organiser')
    search_fields = ('title', 'description', 'location', 'tags')