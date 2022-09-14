from django.urls import path

from .views import MapPageView

urlpatterns = [
    path('', MapPageView.as_view(), name='map'),
]

