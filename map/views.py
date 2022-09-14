from django.views.generic import TemplateView
from django.shortcuts import render
from geopy.geocoders import Nominatim


# Create your views here.
class MapPageView(TemplateView):
    template_name = 'map.html'

    def get_coordinates():
        geocoder = Nominatim(user_agent = 'map')
        location = geocoder.geocode('Alexandra Rd, Swansea SA1 5DZ')
        return(location.latitude, location.longitude)
    
