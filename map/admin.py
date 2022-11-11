from django.contrib import admin
from django import forms
from .models import MapCoordinate
from geopy.geocoders import Nominatim

# Register your models here.
class MapCoordinateAdmin(admin.ModelAdmin):
    list_display = ("participant", "address", "latitude", "longitude",)

    def clean_address(self):
        address = self.cleaned_data['address']
        geocoder = Nominatim(user_agent='map')
        location = geocoder.geocode(address)
        if not location:
            raise forms.ValidationError('You must provide a valid address to proceed.')
        return address

admin.site.register(MapCoordinate, MapCoordinateAdmin)