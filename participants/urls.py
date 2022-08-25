from django.urls import path
from .views import ParticipantFormView

urlpatterns = [
    path('', ParticipantFormView.as_view(), name='participate'),
]

