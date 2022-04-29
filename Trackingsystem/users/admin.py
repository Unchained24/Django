from pyexpat.errors import messages
from django.contrib import admin
from tracking.models import Track
from .models import Message


# Register your models here.

admin.site.register(Message)