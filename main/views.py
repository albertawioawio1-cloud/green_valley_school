from django.shortcuts import render
from .models import Announcement, Event

def home(request):
    announcements = Announcement.objects.filter(is_active=True).order_by('-date_posted')[:3]
    events = Event.objects.order_by('date')[:3]
    return render(request, 'main/home.html', {
        'announcements': announcements,
        'events': events,
    })