from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ParticipantForm

# Create your views here.
class ParticipantFormView(CreateView):
    form_class = ParticipantForm
    success_url= reverse_lazy('dashboard')
    template_name = 'participate.html'


