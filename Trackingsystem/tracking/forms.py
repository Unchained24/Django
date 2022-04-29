from dataclasses import field
from .models import Track
from django import forms


class TrackForm (forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__' 