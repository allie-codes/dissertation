from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.

class ResultsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'results.html'
    login_url = 'account_login'


    