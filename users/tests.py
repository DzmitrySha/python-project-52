import os
import json
from django.test import TestCase
from django.urls import reverse_lazy
from users.models import User

FIXTURES_PATH = 'fixtures'


class TestCreateUser(TestCase):
    # fixtures = ['users.json']

    def setUp(self):
        self.users_url = reverse_lazy('users')
        self.create_url = reverse_lazy('create')
        self.test_user = json.load(
            open(os.path.join(FIXTURES_PATH, "reg_users.json")))

    def test_open_create_page(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(path=self.create_url,
                                    data=self.test_user)
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.get(pk=1)
        self.assertEqual(first=self.user.username,
                         second=self.test_user.get('username')
                         )
        # self.assertContains(response=self.users_url,
        #                     text=self.test_user.get('username')
        #                     )
