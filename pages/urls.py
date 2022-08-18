from django.urls import path

from .views import HomePageView, AboutPageView, DashboardPageView, MapPageView

urlpatterns = [
    path('map/', MapPageView.as_view(), name='map'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]

