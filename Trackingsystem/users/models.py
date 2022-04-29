from pyexpat.errors import messages
from django.db import models
from django.contrib.auth.models import User
from tracking.models import Track
# Create your models here.



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    recipient = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name ="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']