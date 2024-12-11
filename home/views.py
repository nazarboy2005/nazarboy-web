from django.shortcuts import render
from django.views.generic import TemplateView, View
from home.models import HomePageModel, AboutPageModel

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = HomePageModel.objects.first()
        context['name'] = data.name
        context['titles'] = data.titles.all()
        context['first_title'] = context['titles'][0] if context['titles'] else "No one"
        context['quote'] = data.quote
        context['image'] = data.image
        context['social_media_apps'] = data.social_media_apps.all()

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = AboutPageModel.objects.first()
        # context['bio'] = data.bio
        # context['profession'] = data.profession
        # context['image_on_the_left'] = data.image_on_the_left
        # context['text_above_bio'] = data.text_above_bio
        # context['text_below_bio'] = data.text_below_bio
        #
        # context['text_for_smile'] = data.text_for_smile
        # context['number_for_smile'] = data.number_for_smile
        # context['text_for_notebook'] = data.text_for_notebook
        # context['number_for_notebook'] = data.number_for_notebook
        # context['text_for_headphones'] = data.text_for_headphones
        # context['number_for_headphones'] = data.number_for_headphones
        # context['text_for_people'] = data.text_for_people
        # context['number_for_people'] = data.number_for_people

        biography_infos = data.biography_infos.all()
        if biography_infos:
            context['biography_infos_left'] = biography_infos[:(len(biography_infos)+1)//2]
            context['biography_infos_right'] = biography_infos[(len(biography_infos)+1)//2:]

        skills = data.skills.all()
        if skills:
            context['skills_left'] = skills[:(len(skills)+1)//2]
            context['skills_right'] = skills[(len(skills)+1)//2:]

        # context['interests'] = data.interests.all()
        # context['testimonials'] = data.testimonials.all()

        data2 = HomePageModel.objects.first()
        context['social_media_apps'] = data2.social_media_apps.all()

        context['data']=data
        return context








class ContactView(TemplateView):
    template_name = 'contact.html'
