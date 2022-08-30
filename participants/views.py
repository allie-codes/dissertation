from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView
from .forms import ParticipantForm

# Create your views here.
class ParticipantFormView(LoginRequiredMixin, CreateView):
    form_class = ParticipantForm
    success_url= reverse_lazy('participate_success')
    template_name = 'participate.html'
    login_url = 'account_login'

class ParticipateSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'participate_success.html'
    login_url = 'account_login'




