from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView




# @login_required
# def login_redirect(request):
#     if request.user.role == request.user.ADMIN:
#         return redirect('/users/admin/dashboard/')
#     elif request.user.role == request.user.ATTENDEE:
#         return redirect('/users/attendee/dashboard/')
#     return redirect('/users/profile/')

# Create your views here.
# @login_required
# def profile_view(request):
#     user = request.user
#     is_admin = user.is_superadmin and user.is_admin and user.is_superuser
#     is_attendee = not is_admin

#     context = {
#         "is_admin": is_admin,
#         "is_attendee": is_attendee
#     }

#     return render(request, "profile/profile.html", context)

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Redirect based on user's role
        if request.user.is_admin and request.user.role == 'admin':
            return redirect('/users/admin/dashboard/')
        elif not request.user.is_admin and request.user.role == 'attendee':
            return redirect('/users/attendee/dashboard/')  
        return redirect('/users/profile/')     


class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'users/admin_dashboard.html'

    def test_func(self):
        return self.request.user.is_admin

class AttendeeDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'users/attendee_dashboard.html'
    def test_func(self):
        # Only allow attendees to access this view
        return self.request.user.is_attendee
