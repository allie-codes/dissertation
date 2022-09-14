from django.db import models
from participants.models import Participant
from django.urls import reverse
from geopy.geocoders import Nominatim

# Create your models here.
class MapCoordinate(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE, default=True, related_name='result', blank=True)
    address = models.CharField(max_length=250)
    latitude = models.CharField(max_length=50, default=0.0)
    longitude = models.CharField(max_length=50, default=0.0)

    def __str__(self):
        return str(self.latitude and self.longitude)

    def get_absolute_url(self):
        return reverse('home')

    def get_address(self):
        participant = Participant.objects.filter(soil_sample_label=self.participant).first()
        address = participant.address
        return address

    def get_latitude(self):
        address = self.get_address()
        geocoder = Nominatim(user_agent='map')
        location = geocoder.geocode(address)
        return location.latitude

    def get_longitude(self):
        address = self.get_address()
        geocoder = Nominatim(user_agent='map')
        location = geocoder.geocode(address)
        return location.longitude

    def save(self, *args, **kwargs):
        self.address = self.get_address()
        self.latitude = self.get_latitude()
        self.longitude = self.get_longitude()
        super(MapCoordinate, self).save(*args, **kwargs)

    



    


    
    
