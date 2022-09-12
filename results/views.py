from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from participants.models import Participant
from django.db.models import Q
from django.shortcuts import render


# Create your views here.

class ResultsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'results.html'
    login_url = 'account_login'

class SearchResultsPageView(LoginRequiredMixin, ListView):
    model = Participant
    context_object_name = 'participant_list'
    template_name = 'search_results.html'
    login_url = 'account_login'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Participant.objects.filter(
            Q(soil_sample_label__icontains=query)
        )


    