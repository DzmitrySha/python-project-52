import os
import json

from django.test import TestCase
from django.urls import reverse_lazy
from statuses.models import TaskStatus
from users.models import User

FIXTURES_PATH = 'fixtures'


class TestStatusesList(TestCase):
    fixtures = ["users.json", "statuses.json"]

    def setUp(self):
        self.statuses_url = reverse_lazy('statuses')

    def test_open_statuses_page(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(self.statuses_url)
        self.assertEqual(response.status_code, 200)


class TestCreateStatus(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.statuses_url = reverse_lazy('statuses')
        self.create_status_url = reverse_lazy('status_create')
        self.user = User.objects.get(pk=1)
        self.test_status = json.load(
            open(os.path.join(FIXTURES_PATH, "one_status.json")))

    def test_open_create_status_page_without_login(self):
        response = self.client.get(self.create_status_url)
        self.assertEqual(response.status_code, 302)

    def test_open_create_status_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.create_status_url)
        self.assertEqual(response.status_code, 200)

    def test_create_status(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.create_status_url,
                                    data=self.test_status)
        self.assertRedirects(response=response, expected_url=self.statuses_url)
        self.assertEqual(response.status_code, 302)

        self.status = TaskStatus.objects.get(pk=1)
        self.assertEqual(first=self.status.name,
                         second=self.test_status.get('name'))


class TestUpdateStatus(TestCase):
    fixtures = ['users.json', 'statuses.json']

    def setUp(self):
        self.update_status_url = reverse_lazy("status_update", kwargs={"pk": 1})
        self.user = User.objects.get(pk=1)
        self.test_status = json.load(
            open(os.path.join(FIXTURES_PATH, "one_status.json")))

    def test_open_update_statuses_page_without_login(self):
        response = self.client.get(self.update_status_url)
        self.assertEqual(response.status_code, 302)

    def test_open_update_statuses_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.update_status_url)
        self.assertEqual(response.status_code, 200)

    def test_update_status(self):
        self.client.force_login(self.user)
        self.status = TaskStatus.objects.get(pk=1)
        self.assertNotEqual(self.status.name, self.test_status.get("name"))

        response = self.client.post(path=self.update_status_url,
                                    data=self.test_status)
        self.assertEqual(response.status_code, 302)

        self.status = TaskStatus.objects.get(pk=1)
        self.assertEqual(first=self.status.name,
                         second=self.test_status.get('name')
                         )


class TestDeleteStatus(TestCase):
    fixtures = ['users.json', 'statuses.json']

    def setUp(self):
        self.delete_status_url = reverse_lazy("status_delete", kwargs={"pk": 1})
        self.user = User.objects.get(pk=1)

    def test_open_delete_page_without_login(self):
        response = self.client.get(path=self.delete_status_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_delete_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.delete_status_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_delete_status(self):
        self.client.force_login(user=self.user)
        response = self.client.delete(path=self.delete_status_url)
        self.assertEqual(first=response.status_code, second=302)
        with self.assertRaises(TaskStatus.DoesNotExist):
            TaskStatus.objects.get(pk=1)
