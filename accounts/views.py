from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import TemplateView
from .models import User
from .forms import UserUpdateForm
from bookings.models import Booking



class ProfileView(LoginRequiredMixin, View):   
    def get(self, request, *args, **kwargs):
        # Redirect based on user's role
        if request.user.is_admin:
            return redirect('admin-dashboard')
        else:
            return redirect('attendee-dashboard') 

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'users/admin_dashboard.html'
    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  

    def get(self, request):
        total_bookings_analytics = Booking.objects.all().count()
        print(total_bookings_analytics)      
        return render(request, 'users/admin_dashboard.html', {'total_bookings_analytics': total_bookings_analytics})       

class AttendeeDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'users/attendee_dashboard.html'
    def test_func(self):
        # Only allow attendees to access this view
        return self.request.user.role == "attendee"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        print(user.first_name)        
        return context  

    def get(self, request):
        latest_booking = Booking.objects.filter(user=request.user).order_by('-booking_date').first()        
        if latest_booking:
            latest_booking_date = latest_booking.booking_date            
        else:
            latest_booking_date = None  # Or set a default value
        total_bookings_per_attendee = Booking.objects.filter(user=request.user).count() 
        print( total_bookings_per_attendee)       
        return render(request, 'users/attendee_dashboard.html', {'latest_booking_date': latest_booking_date, 'total_bookings_per_attendee': total_bookings_per_attendee})      

class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_profile_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        print(user.first_name)        
        return context

    def get(self, request):
        form = UserUpdateForm(instance=request.user)  # Pre-fill the form with user data
        return render(request, self.template_name, {'user': self.request.user, 'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # Update the user model
            return redirect('my-profile-page')  # Redirect to the same page or another page
        return render(request, self.template_name, {'user': request.user, 'form': form})    

@login_required  
def delete_account(request):
    if request.method == 'POST':
        # get logged in user 
        user = request.user
        # Delete
        user.delete()
        return redirect('account_signup')

    return render(request, 'users/account_delete.html')         

   
       
