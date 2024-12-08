from django.shortcuts import render
from django.views.generic import TemplateView

class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class PortfolioDetailsView(TemplateView):
    template_name = 'portfolio-details.html'


