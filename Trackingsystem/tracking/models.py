from distutils.command.upload import upload
import email
from pickle import TRUE
from unicodedata import name
from django.db import models
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class Track(models.Model):
    trackingID = models.CharField(max_length=6, blank= True, null= True)
    invoice_no = models.IntegerField(default=0, null=True, blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    item_image = models.ImageField(null=True , blank=True, default="default.jpg", upload_to="ItemImage")
    status = models.IntegerField(default=0, blank= True, null= True)
    
    
    shipper_name= models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    receiver_address= models.TextField(max_length=100)

    shipment_type = models.CharField(max_length=50)
    weight =models.CharField(max_length=50)
    comment = models.TextField(null=True, blank=True)
    pickup = models.CharField(max_length=50, blank= True, null= True)
    

    date_created = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.trackingID

    # def save(self, *args, **kwargs):
    #     self.trackingID = self.state + self.shipment_type
    #     super(Track, self).save(*args, **kwargs)