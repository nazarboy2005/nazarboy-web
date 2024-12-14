from django.shortcuts import render
from django.views.generic import TemplateView
from projects.models import ProjectModel, CategoryModel
from home.models import SocialMediaModel

class ProjectsView(TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = ProjectModel.objects.filter(category__to_display=True).distinct()
        context['data'] = data

        social_media_apps = SocialMediaModel.objects.all()
        context['social_media_apps'] = social_media_apps
        return context



class ProjectDetailsView(TemplateView):
    template_name = 'project-details.html'



