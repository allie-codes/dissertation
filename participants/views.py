from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView
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
        return super().form_valid(form)
        
class ParticipateSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'participate_success.html'
    login_url = 'account_login'




