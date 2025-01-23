from . import views
from django.urls import path
from .views import (
    BookingListView,
    BookingDetailView,
    BookingCreateView,
    BookingDeleteView,
)

urlpatterns = [
  path('', BookingListView.as_view(), name='booking-list'),
  path('<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
  path('create/<int:pk>/', BookingCreateView.as_view(), name='booking-create'),
  path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'),
 
]