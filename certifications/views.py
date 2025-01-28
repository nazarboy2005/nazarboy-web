from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CertificationsModel, CategoriesModel, BioModel
from home.models import SocialMediaModel

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
import os
import requests


class CertificationsView(TemplateView):
    template_name = 'certifications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = CertificationsModel.objects.filter(category__to_display=True)
        context['data'] = data
        context['social_media_apps'] = SocialMediaModel.objects.all()
        context['categories'] = CategoriesModel.objects.all()
        context['bio'] = BioModel.objects.first().bio


        return context


class CertificationDetailsView(TemplateView):
    template_name = 'certification-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        certificate_id = self.kwargs.get('id')
        data = CertificationsModel.objects.filter(id=certificate_id).first()
        context['data'] = data
        context['social_media_apps'] = SocialMediaModel.objects.all()
        context['bio'] = BioModel.objects.first().bio

        return context


def download_certificate_view(request, pk):
    certificate = get_object_or_404(CertificationsModel, id=pk)

    # Get Cloudinary file URL
    file_url = certificate.file_to_download.url
    if not file_url:
        return HttpResponse("No file available for download.", status=404)

    # Extract file extension
    file_extension = os.path.splitext(file_url)[1].lower()

    # Determine Content-Type
    content_type_map = {
        '.pdf': 'application/pdf',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png'
    }
    content_type = content_type_map.get(file_extension, 'application/octet-stream')

    # Download the file from Cloudinary
    response = requests.get(file_url)
    if response.status_code != 200:
        return HttpResponse("Failed to fetch the file from Cloudinary.", status=500)

    # Return file as attachment
    filename = f"{certificate.title}{file_extension}"  # Ensuring no duplicate dot
    http_response = HttpResponse(response.content, content_type=content_type)
    http_response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return http_response
