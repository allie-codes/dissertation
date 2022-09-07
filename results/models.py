from xml.etree.ElementTree import tostring
from django.db import models
from participants.models import Participant
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Result(models.Model):
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True, related_name='user')
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

    def __str__(self):
        return self.sample_number

    def get_absolute_url(self):
        return reverse('home')

    def get_participant(self):
        participant = Participant.objects.filter(soil_sample_label=self.sample_label).first()
        return participant

    def save(self, *args, **kwargs):
        self.participant_number = self.get_participant()
        super(Result, self).save(*args, **kwargs)

    
        
