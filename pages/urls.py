from django.urls import path

from .views import HomePageView, AboutPageView, MapPageView, InstructionsPageView

urlpatterns = [
    path('instructions/', InstructionsPageView.as_view(), name='instructions'),
    path('map/', MapPageView.as_view(), name='map'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]

