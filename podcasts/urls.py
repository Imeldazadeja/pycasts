# podcasts/urls.py

from django.urls import path, include

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path('accounts/', include('django.contrib.auth.urls')),
]