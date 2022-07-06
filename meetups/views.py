from curses import flash
from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
# Create your views here.
def index(request):
    meetups = Meetup.objects.all()

    return render(request, "meetups/index.html",{
        'meetups' : meetups
    })


def meetup_details(request,meetup_slug):
    selected_meetups = Meetup.objects.get(slug=meetup_slug)
    return render(request, "meetups/meetup-details.html",{
        'selected_meetups' : selected_meetups
    })
