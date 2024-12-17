from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CertificationsModel, CategoriesModel
from home.models import SocialMediaModel

class CertificationsView(TemplateView):
    template_name = 'certifications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = CertificationsModel.objects.filter(category__to_display=True)
        context['data'] = data
        context['social_media_apps'] = SocialMediaModel.objects.all()
        context['categories'] = CategoriesModel.objects.all()

        return context



class CertificationDetailsView(TemplateView):
    template_name = 'certification-details.html'


