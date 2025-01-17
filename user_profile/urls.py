from . import views
from django.urls import path

urlpatterns = [
  path('', views.profile_view, name='profile'),
  
  path('admin-reports/', views.admin_reports, name='admin_reports'),
  path('my-events/', views.my_events, name='my_events'),
  
 
]