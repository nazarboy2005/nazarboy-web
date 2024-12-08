from django.urls import path
from home.views import HomeView, AboutView, ResumeView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('resume/', ResumeView.as_view(), name='resume'),
]