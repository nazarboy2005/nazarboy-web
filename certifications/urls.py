from django.urls import path
from .views import CertificationsView, CertificationDetailsView, download_certificate_view


app_name = 'certifications'

urlpatterns = [
    path('', CertificationsView.as_view(), name='page'),
    path('details/<int:id>/', CertificationDetailsView.as_view(), name='details'),
    path('download/<int:pk>', download_certificate_view, name='download'),
]