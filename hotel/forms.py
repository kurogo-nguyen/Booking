from django import forms
from .models import Hotel, Room
from user.models import User


class createHotel(forms.ModelForm):
    # manager_id = User.id
    class Meta:
        model = Hotel
        exclude = ['id']


class createRoom(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['id', 'hotel_id']
