from django.test import TestCase


class TestHomePage(TestCase):

    def test_open_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_find_in_html(self):
        response = self.client.get('')
        self.assertContains(response, 'Менеджер задач', status_code=200)
        self.assertTemplateUsed(response, 'index.html')
