from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CertificationsModel, CategoriesModel, BioModel
from home.models import SocialMediaModel

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
import os
import requests
import cloudinary

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

    # ✅ Get the Cloudinary File Public ID
    file_public_id = certificate.file_to_download.public_id  # Get the public ID from CloudinaryField
    if not file_public_id:
        return HttpResponse("No file available for download.", status=404)

    # ✅ Generate a Signed URL for Private Files
    signed_url = cloudinary.utils.cloudinary_url(
        file_public_id,
        resource_type="raw",  # Because it's a PDF
        secure=True,
        sign_url=True  # This signs the URL to grant temporary access
    )[0]

    print(f"Attempting to download from: {signed_url}")  # Debugging output

    try:
        # ✅ Fetch the file from Cloudinary
        response = requests.get(signed_url, stream=True)

        # ✅ Check if the request is successful
        if response.status_code != 200:
            print(f"Cloudinary request failed! Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")  # Print error response
            return HttpResponse("Failed to fetch the file from Cloudinary.", status=500)

        # ✅ Extract file extension & format filename
        file_extension = file_public_id.split('.')[-1]  # Extracting file extension from Public ID
        filename = f"{certificate.title}.{file_extension}"

        # ✅ Set the correct content type
        content_type_map = {
            'pdf': 'application/pdf',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'png': 'image/png'
        }
        content_type = content_type_map.get(file_extension.lower(), 'application/octet-stream')

        # ✅ Return file as an attachment for download
        http_response = HttpResponse(response.content, content_type=content_type)
        http_response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return http_response

    except requests.exceptions.RequestException as e:
        print(f"Exception during file download: {e}")
        return HttpResponse("An error occurred while fetching the file.", status=500)
