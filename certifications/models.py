import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
import os
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import URLValidator


class BioModel(models.Model):
    bio = models.TextField()

    class Meta:
        verbose_name = 'Certifications Bio'
        verbose_name_plural = 'Certifications Bios'



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

    # Allowing either an image or a file
    image = CloudinaryField('image', null=True, blank=True)  # For photos
    file_to_download = CloudinaryField(
        resource_type='raw',
        null=True,
        blank=True,
        validators=[validate_file_extension]
    )  # For PDFs, ZIPs, etc.

    description = models.TextField()
    category = models.ForeignKey(
        CategoriesModel,
        on_delete=models.PROTECT,
        related_name='certifications'
    )
    given_time = models.DateField(default=timezone.now)
    given_by = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True, validators=[URLValidator(message="Enter a valid URL.")])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['-given_time']

    def __str__(self):
        return self.title

        # Custom validation: Ensure at least one of the fields (image or file_to_download) is filled

    def clean(self):
        if not self.image and not self.file_to_download:
            raise ValidationError("You must upload either an image or a file.")

