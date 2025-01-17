from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
@login_required
def profile_view(request):
    user = request.user
    is_admin = user.is_superuser or user.is_staff
    is_attendee = not is_admin

    context = {
        "is_admin": is_admin,
        "is_attendee": is_attendee
    }

    return render(request, "profile/profile.html", context)

@login_required
def admin_reports(request):
    return render(request, 'admin/admin_reports.html')

@login_required
def my_events(request):
    return render(request, 'attendee/my_events.html')

