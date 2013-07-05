# Create your views here.


from django.conf.urls import patterns, url

from .views import \
    (MyModelCreateView, MyModelUpdateView,
    MyModelDetailView, MyModelListView, MyModelDeleteView)


urlpatterns = patterns(
    '',
    url(r'create$',
        MyModelCreateView.as_view(),
        name='create'),
    url(r'edit/(?P<pk>\d+)/$',
        MyModelUpdateView.as_view(),
        name='update'),
    url(r'(?P<pk>\d+)/$',
        MyModelDetailView.as_view(),
        name='detail'),
    url(r'$',
        MyModelListView.as_view(),
        name='list'),
    url(r'delete/(?P<pk>\d+)/$',
        MyModelDeleteView.as_view(),
        name='delete')
)
