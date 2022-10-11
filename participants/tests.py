from django.test import TestCase, Client
from django.urls import reverse
from .models import Participant

# Create your tests here.
class ParticipantTests(TestCase):

    def setUp(self):
        self.participant = Participant.objects.create(
            name = 'John Smith',
        )
    
    def test_participant_listing(self):
        self.assertEqual(f'{self.participant.name}', 'John Smith')

    