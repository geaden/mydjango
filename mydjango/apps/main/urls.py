
from django.conf.urls import patterns, url

from .views import \
    MainPageView, AboutPageView


urlpatterns = patterns(
    '',
    url(r'^$', MainPageView.as_view(),
        name='index'),
    url(r'about/?$', AboutPageView.as_view(),
        name='about'),
)
