from pipes import Template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ResultsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'results.html'
    login_url = 'account_login'

class MapPageView(TemplateView):
    template_name = 'map.html'

class InstructionsPageView(TemplateView):
    template_name = 'instructions.html'
