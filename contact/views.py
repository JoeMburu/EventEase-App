from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")        
        print(f"Received message from {name} ({email}): {message}")

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')         
    return render(request, 'contact/contact.html')