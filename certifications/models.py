import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
import os
from django.db import models


class CategoriesModel(models.Model):
    name = models.CharField(max_length=25)
    to_display = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def joined_name(self):
        return '_'.join(self.name.split(' '))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


def validate_file_extension(value):
    valid_extensions = ['.png', '.jpg', '.jpeg', '.pdf']
    ext = os.path.splitext(value.name)[1]  # Extract file extension
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed extensions are: {", ".join(valid_extensions)}')


class CertificationsModel(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(upload_to='certifications')
    file_to_download = models.FileField(upload_to='certificates-files', null=True, blank=True, validators=[validate_file_extension])
    description = models.TextField()
    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE, related_name='certifications')
    given_time = models.DateField(default=timezone.now)
    given_by = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
