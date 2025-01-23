from . import views
from django.urls import path
from .views import EventDetailView

urlpatterns = [
  path('', views.events, name='event-list'),
  path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
  path('pricing/', views.pricing, name='pricing'),
  path('admin/create', views.create_event, name='admin_event_create')

  #path('', EventListView.as_view(), name='event-list'),
 
 
]