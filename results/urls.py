from django.urls import path

from .views import ResultsPageView

urlpatterns = [
    path('', ResultsPageView.as_view(), name='results'),
]

