from django.test import TestCase
from django.core.urlresolvers import reverse


class MainViewsTestCase(TestCase):
    def test_main_index_view(self):
        url = reverse('main:index')

        response = self.client.\
            get(url)

        self.assertEquals(
            response.status_code,
            200)

    def test_main_about_view(self):
        url = reverse('main:about')

        response = self.client.\
            get(url)

        self.assertEquals(
            response.status_code,
            200)
