from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Booking
from events.models import Event

# Create your views here.
# List all bookings for the logged-in user
class BookingListView(LoginRequiredMixin, ListView):
    pass
    # model = Booking
    # template_name = 'bookings/booking_list.html'
    # context_object_name = 'bookings'

    # def get_queryset(self):
    #     return Booking.objects.filter(user=self.request.user)

# View details of a specific booking
class BookingDetailView(LoginRequiredMixin, DetailView):
    pass
    # model = Booking
    # template_name = 'bookings/booking_detail.html'
    # context_object_name = 'booking'

# Create a new booking
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    event = Event
    template_name = 'bookings/booking_form.html'
    fields = []  # No fields needed; event and user are set programmatically

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     event_id = self.request.GET.get('event_id')
    #     context['event'] = get_object_or_404(Event, id=event_id)
    #     return context

    # def form_valid(self, form):
    #     event_id = self.request.GET.get('event_id')
    #     event = get_object_or_404(Event, id=event_id)
    #     form.instance.user = self.request.user
    #     form.instance.event = event

    #     # Prevent duplicate bookings
    #     if Booking.objects.filter(user=self.request.user, event=event).exists():
    #         return redirect('booking-list')

    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('booking-list')

# Delete a booking
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    # model = Booking
    # template_name = 'bookings/booking_confirm_delete.html'
    # success_url = reverse_lazy('booking-list')
    pass