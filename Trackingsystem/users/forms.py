from random import choices
from sre_parse import State
from .models import Track
from django import forms



STATE = [
    ("AB", "Abia"),
    ("AD", "Adamawa"),
    ("AK", "Akwa Ibom"),
    ("AN", "Anambra"),
    ("BA", "Bauchi"),
    ("BY", "Bayelsa"),
    ("BE", "Benue"),
    ("BO", "Borno"),
    ("CR", "Cross River"),
    ("DE", "Delta"),
    ("EB", "Ebonyi"),
    ("ED", "Edo"),
    ("EK", "Ekiti"),
    ("EN", "Enugu"),
    ("FC", "FCT - Abuja"),
    ("GO", "Gombe"),
    ("IMO", "Imo"),
    ("JI", "Jigawa"),
    ("KD", "Kaduna"),
    ("KN", "Kano"),
    ("KT", "Katsina"),
    ("KE", "Kebbi"),
    ("KO", "Kogi"),
    ("KW", "Kwara"),
    ("LA", "Lagos"),
    ("NA", "Nasarawa"),
    ("NI", "Niger"),
    ("OG", "Ogun"),
    ("ON", "Ondo"),
    ("OS", "Osun"),
    ("OY", "Oyo"),
    ("PL", "Plateau"),
    ("RI", "Rivers"),
    ("SO", "Sokoto"),
    ("TA", "Taraba"),
    ("YO", "Yobe"),
    ("ZA", "Zamfara")
]

SHIPMENT_TYPE = [
    ('STD','Standard Delivery Service (3-5 Working days)'),
    ('SDD','Same Day Delivery'),
    ('OSS','Overnight Shipping Services'),
    ('ROD','Rush and On-Demand Deliveries'),
    ('PS','Parcel Services (7-10 Working days)'),
]
class TrackForm (forms.ModelForm):
    state = forms.ChoiceField(choices = STATE)
    shipment_type = forms.ChoiceField(choices = SHIPMENT_TYPE)
    class Meta:
        model = Track
        fields = ['firstname','lastname','email','item_image','shipper_name','receiver_address','shipment_type','weight','state','city']  