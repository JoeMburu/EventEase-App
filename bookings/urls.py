from . import views
from django.urls import path
from .views import (
    BookingListView,
    BookingDetailView,
    BookingCreateView,
    BookingDeleteView,
    BookingPaymentView,
)

urlpatterns = [
  path('', BookingListView.as_view(), name='booking-list'),
  path('<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
  path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'), 
  path('create/<int:pk>/', BookingCreateView.as_view(), name='booking-create'),  
  path('payment/<int:pk>/', BookingPaymentView.as_view(), name='booking-payment'),
 
]