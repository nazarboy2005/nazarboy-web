from django.shortcuts import render
from django.views.generic import TemplateView


class ServicesView(TemplateView):
    template_name = 'services.html'


class ServiceDetailsView(TemplateView):
    template_name = 'service-details.html'


