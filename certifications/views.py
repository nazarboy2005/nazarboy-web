from django.shortcuts import render
from django.views.generic import TemplateView


class CertificationsView(TemplateView):
    template_name = 'certifications.html'


class CertificationDetailsView(TemplateView):
    template_name = 'certification-details.html'


