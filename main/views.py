from django.shortcuts import render
from .models import Announcement, Event

def home(request):
    announcements = Announcement.objects.all().order_by('-created_at')[:5]
    events = Event.objects.all().order_by('date')[:5]
    context = {
        'announcements': announcements,
        'events': events,
    }
    return render(request, 'main/home.html', context)
