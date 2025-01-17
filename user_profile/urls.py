from . import views
from django.urls import path

urlpatterns = [
  path('', views.profile_view, name='profile'),
 
]