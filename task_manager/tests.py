from django.test import TestCase
from django.utils.translation import gettext_lazy as _


class TestHomePage(TestCase):

    def test_open_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_find_in_html(self):
        response = self.client.get('')
        self.assertContains(response, _('Task manager'), status_code=200)
        self.assertTemplateUsed(response, 'index.html')
