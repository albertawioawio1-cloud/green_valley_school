from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def academics(request):
    return render(request, "main/academics.html")

def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            
            subject_line = f"New Contact Form Submission: {instance.subject}"
            body = f"Name: {instance.name}\nPhone: {instance.phone}\nEmail: {instance.email}\n\nMessage:\n{instance.message}"
            
            send_mail(
                subject=subject_line,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['admin@greenvalleyschool.com'],
                fail_silently=True,
            )
            
            success = True
            form = ContactForm()
    else:
        form = ContactForm()
        
    return render(request, "main/contact.html", {"form": form, "success": success})