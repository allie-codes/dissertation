import secrets
import uuid
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView
from .forms import ParticipantForm
from users.models import CustomUser
from .models import Participant

# Create your views here.
class ParticipantFormView(LoginRequiredMixin, CreateView):
    model = Participant
    form_class = ParticipantForm
    success_url= reverse_lazy('participate_success')
    template_name = 'participate.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.soil_sample_label = secrets.token_hex(nbytes=4).upper()
        form.instance.sample_label = uuid.uuid4()
        return super().form_valid(form)
        
class ParticipateSuccessView(LoginRequiredMixin, ListView):
    template_name = 'participate_success.html'
    login_url = 'account_login'
    model = Participant
    context_object_name = 'participant_id'

    def get_queryset(self):
        participant_id = str(Participant.objects.filter(user=self.request.user).order_by('-created').values_list('soil_sample_label').first())

        remove_characters = ['(', '\'', ',', ')']

        for character in remove_characters:
            participant_id = participant_id.replace(character, '')
        
        return participant_id






