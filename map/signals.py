from participants.models import Participant
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MapCoordinate

@receiver(post_save, sender=Participant)
def map_coordinate_create(sender, instance=None, created=False, **kwargs):
    if created:
        MapCoordinate.objects.create(participant=instance, address=Participant.address)



