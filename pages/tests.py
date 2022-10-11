from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView, InstructionsPageView

# Create your tests here.
class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )
    
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )

class InstructionsPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('instructions')
        self.response = self.client.get(url)

    def test_instructionspage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_instructionspage_template(self):
        self.assertTemplateUsed(self.response, 'instructions.html')
    
    def test_instructionspage_contains_correct_html(self):
        self.assertContains(self.response, 'Instructions')

    def test_instructionspage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )
    
    def test_instructionspage_url_resolves_aboutpageview(self):
        view = resolve('/instructions/')
        self.assertEqual(
            view.func.__name__,
            InstructionsPageView.as_view().__name__
        )