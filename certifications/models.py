import datetime
from django.utils import timezone

from django.db import models


class CategoriesModel(models.Model):
    name = models.CharField(max_length=25)
    to_display = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class CertificationsModel(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(upload_to='certifications')
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
