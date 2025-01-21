from django.shortcuts import render, redirect
from .forms import EventRegisterForm
from accounts.models import User
from .models import Event

# Create your views here.
def events(request):
    events = Event.objects.all()
    context =  {
        'events': events
    }      
    
    return render(request, 'events/events.html', context)

def pricing(request):
    return render(request, 'events/pricing.html')

def register_event(request):
    if request.method == 'POST':
        form = EventRegisterForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user
            form.save() 
            return redirect('register_event')

    else:
        form = EventRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'events/register_event.html', context)    