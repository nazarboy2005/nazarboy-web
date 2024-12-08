from django.urls import path
from .views import PortfolioView, PortfolioDetailsView


app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioView.as_view(), name='page'),
    path('details/', PortfolioDetailsView.as_view(), name='details'),
]