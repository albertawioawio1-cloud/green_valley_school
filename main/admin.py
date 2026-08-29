from django.contrib import admin
from .models import ContactMessage, Announcement, Event

admin.site.register(ContactMessage)
admin.site.register(Announcement)
admin.site.register(Event)