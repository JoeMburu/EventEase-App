from django.contrib import admin
from .models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'event', 'price', 'reminder', 'payment_status', 'booking_status', 'booking_date')
    list_filter = ('booking_status', 'payment_status', 'booking_date')
    search_fields = ('email', 'title')
    ordering = ('-booking_date',)

admin.site.register(Booking, BookingAdmin)