from django.test import TestCase

from ..models import MyModel


class MyModelTestCase(TestCase):
    def test_mymodel_create(self):
        MyModel.objects.create(
            title=u'foo')

        self.assertEquals(
            MyModel.objects.all().
            count(),
            1)
