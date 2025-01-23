from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventRegisterForm
from accounts.models import User
from .models import Event
from django.views.generic import ListView, DetailView, CreateView, DeleteView

# Create your views here.
def events(request):
    events = Event.objects.all()
    context =  {
        'events': events
    }      
    
    return render(request, 'events/event-list.html', context)

def pricing(request):
    return render(request, 'events/pricing.html')

@login_required
def create_event(request):
    if request.user.is_admin:
        if request.method == 'POST':
            form = EventRegisterForm(request.POST, request.FILES)            
            if form.is_valid():
                event = form.save(commit=False)
                event.organiser = request.user
                form.save()                 
                return redirect('event-list') # You cN CHANGE THIS LATER
        else:
            form = EventRegisterForm()   
        context = {
            'form': form
         }
        return render(request, 'events/admin_event_create.html', context)            
    else:
       return redirect('event-list')  # Change this later

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
     