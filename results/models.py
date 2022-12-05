from django.db import models
from participants.models import Participant
from django.urls import reverse
import random
import math
from geopy.geocoders import Nominatim
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Result(models.Model):
    participant_number = models.ForeignKey(Participant, on_delete=models.CASCADE, default=True, related_name='participant_number', blank=True)
    sample_label = models.CharField(_('sample_label'), max_length=50, blank=True)
    sample_number = models.CharField(_('sample_number'), max_length=250)
    na = models.CharField(_('na'), max_length=250)
    mg = models.CharField(_('mg'), max_length=250)
    al = models.CharField(_('al'), max_length=250)
    si = models.CharField(_('si'), max_length=250)
    p = models.CharField(_('p'), max_length=250)
    s = models.CharField(_('s'), max_length=250)
    cl = models.CharField(_('cl'), max_length=250)
    k = models.CharField(_('k'), max_length=250)
    ca = models.CharField(_('ca'), max_length=250)
    ti = models.CharField(_('ti'), max_length=250)
    v = models.CharField(_('v'), max_length=250)
    cr = models.CharField(_('cr'), max_length=250)
    mn = models.CharField(_('mn'), max_length=250)
    fe = models.CharField(_('fe'), max_length=250)
    co = models.CharField(_('co'), max_length=250)
    ni = models.CharField(_('ni'), max_length=250)
    cu = models.CharField(_('cu'), max_length=250)
    zn = models.CharField(_('zn'), max_length=250)
    ga = models.CharField(_('ga'), max_length=250)
    ge = models.CharField(_('ge'), max_length=250)
    As = models.CharField(_('As'), max_length=250)
    se = models.CharField(_('se'), max_length=250)
    br = models.CharField(_('br'), max_length=250)
    rb = models.CharField(_('rb'), max_length=250)
    sr = models.CharField(_('sr'), max_length=250)
    y = models.CharField(_('y'), max_length=250)
    nb = models.CharField(_('nb'), max_length=250)
    mo = models.CharField(_('mo'), max_length=250)
    ru = models.CharField(_('ru'), max_length=250)
    rh = models.CharField(_('rh'), max_length=250)
    pd = models.CharField(_('pd'), max_length=250)
    ag = models.CharField(_('ag'), max_length=250)
    cd = models.CharField(_('cd'), max_length=250)
    In = models.CharField(_('In'), max_length=250)
    sn = models.CharField(_('sn'), max_length=250)
    sb = models.CharField(_('sb'), max_length=250)
    te = models.CharField(_('te'), max_length=250)
    i = models.CharField(_('i'), max_length=250)
    cs = models.CharField(_('cs'), max_length=250)
    ba = models.CharField(_('ba'), max_length=250)
    la = models.CharField(_('la'), max_length=250)
    ce = models.CharField(_('ce'), max_length=250)
    pr = models.CharField(_('pr'), max_length=250)
    nd = models.CharField(_('nd'), max_length=250)
    hf = models.CharField(_('hf'), max_length=250)
    ta = models.CharField(_('ta'), max_length=250)
    w = models.CharField(_('w'), max_length=250)
    pt = models.CharField(_('pt'), max_length=250)
    au = models.CharField(_('au'), max_length=250)
    hg = models.CharField(_('hg'), max_length=250)
    tl = models.CharField(_('tl'), max_length=250)
    pb = models.CharField(_('pb'), max_length=250)
    bi = models.CharField(_('bi'), max_length=250)
    th = models.CharField(_('th'), max_length=250)
    u = models.CharField(_('u'), max_length=250)
    latitude = models.CharField(_('latitude'), max_length=50, default=0.0)
    longitude = models.CharField(_('longitude'), max_length=50, default=0.0)
    rand_lat = models.FloatField(_('rand_lat'), blank=True, default=0.0)
    rand_long = models.FloatField(_('rand_long'), blank=True, default=0.0)

    def __str__(self):
        return self.sample_number

    def get_absolute_url(self):
        return reverse('home')

    def get_participant(self):
        participant = Participant.objects.filter(soil_sample_label=self.sample_label).first()
        return participant

    def get_address(self):
        participant = self.participant_number
        return participant.address

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

    def generate_random_latitude(self):
        radius = 7000
        radius_in_degrees = radius/111300
        r = radius_in_degrees
        x0 = float(self.get_latitude())
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = r * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        random_lat = x + x0
        return float(random_lat)

    def generate_random_longitude(self):
        radius = 7000
        radius_in_degrees = radius/111300
        r = radius_in_degrees
        y0 = float(self.get_longitude())
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = r * math.sqrt(u)
        t = 2 * math.pi * v
        y = w * math.sin(t)
        random_long = y + y0
        return float(random_long)


    def save(self, *args, **kwargs):
        self.participant_number = self.get_participant()
        self.latitude = self.get_latitude()
        self.longitude = self.get_longitude()
        self.rand_lat = self.generate_random_latitude()
        self.rand_long = self.generate_random_longitude()
        super(Result, self).save(*args, **kwargs)

    
        
