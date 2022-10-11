from django.test import TestCase, Client
from django.urls import reverse
from .models import Result

# Create your tests here.
class ResultTests(TestCase):

    def setUp(self):
        self.result = Result.objects.create(
            na = 1.274,
        )
    
    def test_result_listing(self):
        self.assertEqual(f'{self.result.na}', 1.274)
