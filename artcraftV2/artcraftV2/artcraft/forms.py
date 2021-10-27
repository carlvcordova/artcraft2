from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import *


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('firstName','lastName','birthDate','address','phoneNumber','username','password')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('firstName','lastName', 'email', 'address', 'phoneNumber', 'username', 'password')

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ( 'year', 'title', 'price','type', 'description', 'artistID')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('orderPrice','orderDate','artworkID','customerID')