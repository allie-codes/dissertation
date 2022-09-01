from django.db import models
from participants.models import Participant
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Result(models.Model):
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True, related_name='user')
    participant_number = models.ForeignKey(Participant, on_delete=models.CASCADE, default=True, related_name='participant_number')
    name = models.CharField(max_length=50, blank=True)
    sample_number = models.CharField(max_length=50)
    na = models.CharField(max_length=20)
    mg = models.CharField(max_length=20)
    al = models.CharField(max_length=20)
    si = models.CharField(max_length=20)
    p = models.CharField(max_length=20)
    s = models.CharField(max_length=20)
    cl = models.CharField(max_length=20)
    k = models.CharField(max_length=20)
    ca = models.CharField(max_length=20)
    ti = models.CharField(max_length=20)
    v = models.CharField(max_length=20)
    cr = models.CharField(max_length=20)
    mn = models.CharField(max_length=20)
    fe = models.CharField(max_length=20)
    co = models.CharField(max_length=20)
    ni = models.CharField(max_length=20)
    cu = models.CharField(max_length=20)
    zn = models.CharField(max_length=20)
    ga = models.CharField(max_length=20)
    ge = models.CharField(max_length=20)
    As = models.CharField(max_length=20)
    se = models.CharField(max_length=20)
    br = models.CharField(max_length=20)
    rb = models.CharField(max_length=20)
    sr = models.CharField(max_length=20)
    y = models.CharField(max_length=20)
    nb = models.CharField(max_length=20)
    mo = models.CharField(max_length=20)
    ru = models.CharField(max_length=20)
    rh = models.CharField(max_length=20)
    pd = models.CharField(max_length=20)
    ag = models.CharField(max_length=20)
    cd = models.CharField(max_length=20)
    In = models.CharField(max_length=20)
    sn = models.CharField(max_length=20)
    sb = models.CharField(max_length=20)
    te = models.CharField(max_length=20)
    i = models.CharField(max_length=20)
    cs = models.CharField(max_length=20)
    ba = models.CharField(max_length=20)
    la = models.CharField(max_length=20)
    ce = models.CharField(max_length=20)
    pr = models.CharField(max_length=20)
    nd = models.CharField(max_length=20)
    hf = models.CharField(max_length=20)
    ta = models.CharField(max_length=20)
    w = models.CharField(max_length=20)
    pt = models.CharField(max_length=20)
    au = models.CharField(max_length=20)
    hg = models.CharField(max_length=20)
    tl = models.CharField(max_length=20)
    pb = models.CharField(max_length=20)
    bi = models.CharField(max_length=20)
    th = models.CharField(max_length=20)
    u = models.CharField(max_length=20)

    def __str__(self):
        return self.sample_number

    def get_absolute_url(self):
        return reverse('home')

    def get_participant_name(self):
        name = Participant.name
        return name

    def save(self, *args, **kwargs):
        self.name = self.get_participant_name()
        super(Result, self).save(*args, **kwargs)

