#from . import views
from django.urls import path
from .views import ProfileView, AdminDashboardView, AttendeeDashboardView

urlpatterns = [
  path('profile/', ProfileView.as_view(), name='profile'),
  path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
  path('attendee/dashboard/', AttendeeDashboardView.as_view(), name='attendee-dashboard')
 
]

# /accounts/login/
# /accounts/logout/
# /accounts/signup/
# /accounts/password/change/
# /accounts/password/reset/
# AllAuth brings these paths by default.