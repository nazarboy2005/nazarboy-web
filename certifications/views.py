from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CertificationsModel, CategoriesModel
from home.models import SocialMediaModel

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
import os


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        certificate_id = self.kwargs.get('id')
        data = CertificationsModel.objects.filter(id=certificate_id).first()
        context['data'] = data
        context['social_media_apps'] = SocialMediaModel.objects.all()
        return context




def download_certificate_view(request, pk):
    certificate = get_object_or_404(CertificationsModel, id=pk)

    file_path = certificate.file_to_download.path
    print(file_path)
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.pdf':
        content_type = 'application/pdf'
    elif file_extension in ['.jpg', '.jpeg']:
        content_type = 'image/jpeg'
    else:
        content_type = 'image/png'

    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{certificate.title}.{file_extension}"'
        return response

