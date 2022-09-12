from django.urls import path

from .views import ResultsPageView, SearchResultsPageView

urlpatterns = [
    path('', ResultsPageView.as_view(), name='results'),
    path('search/', SearchResultsPageView.as_view(), name='search_results'),
]

