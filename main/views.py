from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Green Valley School - Website setup is complete!")
