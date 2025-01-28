from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Booking
from events.models import Event
from .forms import BookingForm
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
# List all bookings for the logged-in user
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unpaid_bookings'] = Booking.objects.filter(user=self.request.user, booking_status='PENDING', payment_status='NOT_PAID')
        context['paid_bookings'] = Booking.objects.filter(user=self.request.user, booking_status='CONFIRMED', payment_status='PAID') 
        context['canceled_bookings'] = Booking.objects.filter(user=self.request.user, booking_status='CANCELED', payment_status='REFUNDED')        
        return context    

# View details of a specific booking
class BookingDetailView(LoginRequiredMixin, DetailView):
    pass
    # model = Booking
    # template_name = 'bookings/booking_detail.html'
    # context_object_name = 'booking'

# Create a new booking
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'    

    def get_initial(self):
        """
        Prepopulate the form's price field with the event's price.
        """
        event = get_object_or_404(Event, pk=self.kwargs['pk'])
        initial = super().get_initial()
        initial['price'] = event.price        
        return initial

    def form_valid(self, form):
        """
        Set the event and user for the booking before saving.
        """
        event = get_object_or_404(Event, pk=self.kwargs['pk'])
        form.instance.event = event
        form.instance.price = event.price
        form.instance.user = self.request.user
        booking = form.save()     
        #booking_payment_url = reverse('booking-payment', kwargs={'pk': booking.pk})  
        return redirect('booking-list')

    def get_context_data(self, **kwargs):
        """
        Pass the event and user to the context for rendering in the template.
        """
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['pk'])
        context['user'] = self.request.user
        context['organiser'] = get_object_or_404(Event, pk=self.kwargs['pk']).organiser        
        return context    

   

# Delete a booking
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    # model = Booking
    # template_name = 'bookings/booking_confirm_delete.html'
    # success_url = reverse_lazy('booking-list')
    pass

# Booking payment
class BookingPaymentView(TemplateView):
    
    template_name = 'bookings/booking_payment.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking_id = kwargs.get('pk')  # Get the booking ID from the URL
        booking = get_object_or_404(Booking, pk=booking_id)
        context['unpaid_booking'] = booking
        return context

    def post(self, request, *args, **kwargs):
        booking_id = kwargs.get('pk')  # Get the booking ID from the URL
        print("id: ", booking_id)
        booking = get_object_or_404(Booking, pk=booking_id)

        # Update the payment status
        booking.payment_status = 'PAID'
        booking.save()

        # Optionally, set booking status to 'Confirmed' as well
        booking.booking_status = 'CONFIRMED'
        booking.save()

        # Display a success message
        messages.success(request, "Payment confirmed successfully!")

        # Redirect to the booking listing
        return redirect('booking-list')  

# Booking payment
class BookingCancelView(TemplateView):
    
    template_name = 'bookings/booking_cancel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking_id = kwargs.get('pk')  # Get the booking ID from the URL
        booking = get_object_or_404(Booking, pk=booking_id)
        context['cancel_booking'] = booking
        return context

    def post(self, request, *args, **kwargs):
        booking_id = kwargs.get('pk')  # Get the booking ID from the URL
        booking = get_object_or_404(Booking, pk=booking_id)

        # Update the payment status
        booking.payment_status = 'REFUNDED'
        booking.save()

        # Optionally, set booking status to 'Confirmed' as well
        booking.booking_status = 'CANCELED'
        booking.save()

        # Display a success message
        messages.success(request, "You have successfully canceled your booking!")

        # Redirect to the booking listing
        return redirect('booking-list')          