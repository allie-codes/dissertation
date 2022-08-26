from django.urls import path
from .views import ParticipantFormView, ParticipateSuccessView

urlpatterns = [
    path('success/', ParticipateSuccessView.as_view(), name='participate_success'),
    path('', ParticipantFormView.as_view(), name='participate'),
]

