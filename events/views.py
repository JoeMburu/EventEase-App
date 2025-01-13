from django.shortcuts import render

# Create your views here.
def events(request):
    return render(request, 'events/events.html')

def pricing(request):
    return render(request, 'events/pricing.html')