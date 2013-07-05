from django.test import TestCase

from django.core.urlresolvers import reverse

from ..models import MyModel
from ..views import MyModelCreateView, \
    MyModelUpdateView, MyModelDetailView, \
    MyModelListView, MyModelDeleteView


class MainViewsTestCase(TestCase):
    def setUp(self):
        self.my_model = MyModel.objects.\
            create(
                title=u'foo')
        self.create_url = reverse(
            'mymodel:create')
        self.detail_url = reverse(
            'mymodel:detail',
            args=[self.my_model.pk])
        self.list_url = reverse(
            'mymodel:list')
        self.update_url = reverse(
            'mymodel:update',
            args=[self.my_model.pk])
        self.delete_url = reverse(
            'mymodel:delete',
            args=[self.my_model.pk])

    def test_mymodel_create(self):
        post = {'title': u'bar'}
        response = self.client.\
            post(self.create_url, post)

        self.assertEquals(
            response.status_code,
            302)

        self.assertEquals(
            MyModel.objects.all().
            count(),
            2)

    def test_mymodel_detail(self):
        response = self.client.\
            get(self.detail_url)

        self.assertEquals(
            response.status_code,
            200)

        self.assertEquals(
            response.context['object'],
            self.my_model)

    def test_mymodel_list(self):
        response = self.client.\
            get(self.list_url)

        self.assertEquals(
            response.status_code,
            200)

        self.assertEquals(
            len(response.context['object_list']),
            1)

    def test_mymodel_update(self):
        post = {'title': u'foobar'}

        response = self.client.\
            post(self.update_url, post)

        self.assertEquals(
            response.status_code,
            302)

        my_model = MyModel.objects.get(
            pk=self.my_model.pk)

        self.assertEquals(
            my_model.title,
            u'foobar')
