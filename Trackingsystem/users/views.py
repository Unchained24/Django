from email import message
import email
from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.template import context
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Track, Message
from .forms import TrackForm
import random
import string
from django.core.mail import send_mail

 

# Create your views here.
def loginUser(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
           messages.error(request,'username or passowrd is incorrect')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'Logout Sucessful')
    return redirect('login')

@login_required(login_url="login")
def dashboard(request):
    shipdetailsnew = Track.objects.all()
    context = {'ship': shipdetailsnew}
    return render(request, 'users/dashboard.html', context)


def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_uppercase) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  


@login_required(login_url="login")
def addshipment(request):
    tid = 0
    form = TrackForm()
    if request.method == 'POST' :
        form = TrackForm(request.POST)
        if form.is_valid():
           
            # form.save()

            fn = form.cleaned_data.get('firstname')
            ln = form.cleaned_data.get('lastname')
            em = form.cleaned_data.get('email')
            im = form.cleaned_data.get('item_image')
            sn = form.cleaned_data.get('shipper_name')
            ra = form.cleaned_data.get('receiver_address')
            sty = form.cleaned_data.get('shipment_type')
            we = form.cleaned_data.get('weight')
            st = form.cleaned_data.get('state')
            ci = form.cleaned_data.get('city')
            
            tid = st + sty + random_string(5, 3)

            track = Track(firstname = fn, lastname = ln, email = em,
             item_image = im, shipper_name = sn, receiver_address = ra,
              shipment_type = sty, weight = we, state = st, city = ci, trackingID = tid)

            track.save()
            email = request.POST['email']

            send_mail(
                'Tracking ID',
                f'Thank you for trusting us with your package, your TRACKINGID is {{tid}}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )


            messages.success(request, 'Tracking ID has been sucessfully sent to email')
            return redirect('addshipment')

    context={'form':form, 'tid':tid}
    return render(request, 'users/addshipment.html', context)



@login_required(login_url="login")
def updateshipment(request, pk):
    track = Track.objects.get(id = pk)
    form = TrackForm(instance=track)
    if request.method == 'POST' :
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('addshipment')

    context={'form':form}
    return render(request, 'users/addshipment.html', context)


@login_required(login_url="login")
def listshipment(request):
    shipment = Track.objects.all()
    context = {'shipment': shipment}
    return render(request, 'users/listshipment.html', context)

@login_required(login_url="login")
def viewshipment(request, pk):
    viewship = Track.objects.get(id = pk)
    context = {'viewship': viewship}

    return render(request, 'users/viewshipment.html', context)

@login_required(login_url="login")
def deleteshipment(request, pk):
    track = Track.objects.get(id = pk)
    if request.method == 'POST':
        track.delete()
        return redirect('listshipment')
    context = {'track': track}

    return render(request, 'users/deleteshipment.html', context)

@login_required(login_url="login")
def queryshipment(request):
    if request.method == "POST":
        search = request.POST['search']
        track = Track.objects.filter(trackingID__iexact = search)
        if len(track) == 0:
            found = False
        else:
            found = True
        
        print(found)
        print(search)
    context = {'track': track, 'found':found, 'search':search}
    return render(request, 'users/queryshipment.html', context)

@login_required(login_url="login")
def searchshipment(request):
    
    return render(request, 'users/searchshipment.html')

@login_required(login_url="login")
def inbox(request):
    user = request.user
    messagesReqeust = user.messages.all()
    unreadCount = messagesReqeust.filter(is_read = False).count()

    context = {'messagesReqeust': messagesReqeust, 'unreadCount': unreadCount}
    return render (request, 'users/inbox.html', context)