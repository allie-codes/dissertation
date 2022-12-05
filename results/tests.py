from django.test import TestCase, Client
from django.urls import reverse
from .models import Result
from participants.models import Participant

# Create your tests here.
class ResultTests(TestCase):

    def setUp(self):
        self.result = Result.objects.create(
            sample_label = Participant.objects.create(name='John Smith', email='john@email.com', address = 'Singleton Park, Sketty, Swansea SA2 8PP', sample_1_description = 'back garden', sample_2_description = 'left side garden', sample_3_description = 'right side garden', sample_4_description = 'front garden', sample_5_description = 'vegetable patch', agreement = True),
            na = '1.274',
            mg = '0.34',
            al = '4.36'
        )
    
    def test_result_listing(self):
        self.assertEqual(f'{self.result.na}', '1.274')
