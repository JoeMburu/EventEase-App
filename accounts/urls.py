from . import views
from django.urls import path
from .views import ProfileView, AdminDashboardView, AttendeeDashboardView, MyPageView

urlpatterns = [
 
  path('my-page/', MyPageView.as_view(), name='my-profile-page'),
  path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
  path('attendee/dashboard/', AttendeeDashboardView.as_view(), name='attendee-dashboard'),
  path('profile/', ProfileView.as_view(), name='profile'),
 
]

# /accounts/login/
# /accounts/logout/
# /accounts/signup/
# /accounts/password/change/
# /accounts/password/reset/
# AllAuth brings these paths by default.