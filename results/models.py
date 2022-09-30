from django.db import models
from participants.models import Participant
from map.models import MapCoordinate
from django.urls import reverse
import random
import sys
import math

# Create your models here.
class Result(models.Model):
    participant_number = models.ForeignKey(Participant, on_delete=models.CASCADE, default=True, related_name='participant_number', blank=True)
    sample_label = models.CharField(max_length=50, blank=True)
    sample_number = models.CharField(max_length=250)
    na = models.CharField(max_length=250)
    mg = models.CharField(max_length=250)
    al = models.CharField(max_length=250)
    si = models.CharField(max_length=250)
    p = models.CharField(max_length=250)
    s = models.CharField(max_length=250)
    cl = models.CharField(max_length=250)
    k = models.CharField(max_length=250)
    ca = models.CharField(max_length=250)
    ti = models.CharField(max_length=250)
    v = models.CharField(max_length=250)
    cr = models.CharField(max_length=250)
    mn = models.CharField(max_length=250)
    fe = models.CharField(max_length=250)
    co = models.CharField(max_length=250)
    ni = models.CharField(max_length=250)
    cu = models.CharField(max_length=250)
    zn = models.CharField(max_length=250)
    ga = models.CharField(max_length=250)
    ge = models.CharField(max_length=250)
    As = models.CharField(max_length=250)
    se = models.CharField(max_length=250)
    br = models.CharField(max_length=250)
    rb = models.CharField(max_length=250)
    sr = models.CharField(max_length=250)
    y = models.CharField(max_length=250)
    nb = models.CharField(max_length=250)
    mo = models.CharField(max_length=250)
    ru = models.CharField(max_length=250)
    rh = models.CharField(max_length=250)
    pd = models.CharField(max_length=250)
    ag = models.CharField(max_length=250)
    cd = models.CharField(max_length=250)
    In = models.CharField(max_length=250)
    sn = models.CharField(max_length=250)
    sb = models.CharField(max_length=250)
    te = models.CharField(max_length=250)
    i = models.CharField(max_length=250)
    cs = models.CharField(max_length=250)
    ba = models.CharField(max_length=250)
    la = models.CharField(max_length=250)
    ce = models.CharField(max_length=250)
    pr = models.CharField(max_length=250)
    nd = models.CharField(max_length=250)
    hf = models.CharField(max_length=250)
    ta = models.CharField(max_length=250)
    w = models.CharField(max_length=250)
    pt = models.CharField(max_length=250)
    au = models.CharField(max_length=250)
    hg = models.CharField(max_length=250)
    tl = models.CharField(max_length=250)
    pb = models.CharField(max_length=250)
    bi = models.CharField(max_length=250)
    th = models.CharField(max_length=250)
    u = models.CharField(max_length=250)
    latitude = models.CharField(max_length=50, default=0.0)
    longitude = models.CharField(max_length=50, default=0.0)
    rand_lat = models.FloatField(blank=True, default=0.0)
    rand_long = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.sample_number

    def get_absolute_url(self):
        return reverse('home')

    def get_participant(self):
        participant = Participant.objects.filter(soil_sample_label=self.sample_label).first()
        return participant

    def get_latitude(self):
        map_coordinate = MapCoordinate.objects.filter(participant = self.participant_number).first()
        latitude = map_coordinate.latitude
        return latitude

    def get_longitude(self):
        map_coordinate = MapCoordinate.objects.filter(participant = self.participant_number).first()
        longitude = map_coordinate.longitude
        return longitude

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

    
        
