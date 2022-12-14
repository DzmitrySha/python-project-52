import os
import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

FIXTURES_PATH = 'fixtures'


class TestCreateUser(TestCase):

    def setUp(self):
        self.create_url = reverse_lazy('create')
        self.test_user = json.load(
            open(os.path.join(FIXTURES_PATH, "one_user.json")))

    def test_open_create_page(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(path=self.create_url, data=self.test_user)
        self.assertEqual(response.status_code, 302)
        self.user = get_user_model().objects.get(pk=1)
        self.assertEqual(first=self.user.username,
                         second=self.test_user.get('username')
                         )


class TestUpdateUser(TestCase):
    fixtures = ['users.json']

    def setUp(self) -> None:
        self.update_url = reverse_lazy('update', kwargs={"pk": 1})
        self.user = get_user_model().objects.get(pk=1)
        self.test_user = json.load(
            open(os.path.join(FIXTURES_PATH, "one_user.json")))

    def test_open_update_page(self):
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 302)

    def test_update_user(self):
        self.client.force_login(self.user)
        self.assertNotEqual(self.user.username, self.test_user.get("username"))
        response = self.client.post(self.update_url, data=self.test_user)
        self.assertEqual(response.status_code, 302)
        self.user = get_user_model().objects.get(pk=1)
        self.assertEqual(self.user.username, self.test_user.get("username"))


class TestDeleteUser(TestCase):
    fixtures = ['users.json']

    def setUp(self) -> None:
        self.delete_url = reverse_lazy("delete", kwargs={"pk": 1})
        self.test_user = get_user_model().objects.get(pk=1)

    def test_open_delete_page(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        self.client.force_login(self.test_user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(get_user_model().DoesNotExist):
            get_user_model().objects.get(pk=1)
