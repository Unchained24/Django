
from django.shortcuts import render, redirect
from django.template import context
from .models import Track
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import TrackForm
# Create your views here.

def home(request):
    return render(request, 'tracking/home.html')

def about(request):
    return render(request, 'tracking/about.html')

def service(request):
    return render(request, 'tracking/services.html')

def contactUs(request):
    return render(request, 'tracking/contactus.html')

  
def search(request):
    # form=TrackForm()
    if request.method == "POST":
        search =request.POST['search']
        track = Track.objects.filter(trackingID__iexact = search)
        if len(track) == 0:
            found = False
        else:
            found = True

        
    context = {'track':track, 'found':found, 'search':search}
    return render(request, 'tracking/track.html',context)

def formtest(request):
    form = TrackForm()
    context={'form':form}

    return render(request, 'tracking/form.html', context)