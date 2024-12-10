from django.contrib import admin
from .models import HomePageModel, SocialMediaModel, TitleModel, InterestsModel, AboutPageModel, SkillsModel, \
    BiographyModel, TestimonialsModel


# ----------------Home Page Admin----------------#
class SocialMediaModelAdmin(admin.StackedInline):
    model = SocialMediaModel


class TitleModelAdmin(admin.StackedInline):
    model = TitleModel


@admin.register(HomePageModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [SocialMediaModelAdmin, TitleModelAdmin]


# ----------------About Page Admin----------------#
class BiographyModelAdmin(admin.StackedInline):
    model = BiographyModel


class SkillsModelAdmin(admin.StackedInline):
    model = SkillsModel


class InterestsModelAdmin(admin.StackedInline):
    model = InterestsModel


class TestimonialsModelAdmin(admin.StackedInline):
    model = TestimonialsModel


@admin.register(AboutPageModel)
class AboutPageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [BiographyModelAdmin, SkillsModelAdmin, InterestsModelAdmin, TestimonialsModelAdmin]
