from . import views
from django.urls import path
from .views import EventDetailView, EventDeleteView

urlpatterns = [
  path('', views.events, name='event-list'),
  path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
  path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'), 
  path('pricing/', views.pricing, name='pricing'),
  path('admin/create', views.create_event, name='admin_event_create')

  #path('', EventListView.as_view(), name='event-list'),
 
 
]