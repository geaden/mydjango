from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'main/index.html'


class AboutPageView(TemplateView):
    template_name = 'main/about.html'
