import os
import json

from django.test import TestCase
from django.urls import reverse_lazy
from labels.models import TaskLabels
from users.models import User
from task_manager.settings import FIXTURE_DIRS


class TestLabelsList(TestCase):
    fixtures = ["users.json", "labels.json"]

    def setUp(self):
        self.labels_url = reverse_lazy('labels')

    def test_open_labels_page(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(self.labels_url)
        self.assertEqual(response.status_code, 200)


class TestCreateLabel(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.labels_url = reverse_lazy('labels')
        self.create_label_url = reverse_lazy('label_create')
        self.user = User.objects.get(pk=1)
        self.test_label = json.load(
            open(os.path.join(FIXTURE_DIRS[0], "one_label.json")))

    def test_open_create_label_page_without_login(self):
        response = self.client.get(self.create_label_url)
        self.assertEqual(response.status_code, 302)

    def test_open_create_label_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.create_label_url)
        self.assertEqual(response.status_code, 200)

    def test_create_label(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.create_label_url,
                                    data=self.test_label)
        self.assertRedirects(response=response, expected_url=self.labels_url)
        self.assertEqual(response.status_code, 302)

        self.label = TaskLabels.objects.get(pk=1)
        self.assertEqual(first=self.label.name,
                         second=self.test_label.get('name'))


class TestUpdateLabel(TestCase):
    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        self.update_label_url = reverse_lazy("label_update", kwargs={"pk": 1})
        self.user = User.objects.get(pk=1)
        self.test_label = json.load(
            open(os.path.join(FIXTURE_DIRS[0], "one_label.json")))

    def test_open_update_label_page_without_login(self):
        response = self.client.get(self.update_label_url)
        self.assertEqual(response.status_code, 302)

    def test_open_update_label_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.update_label_url)
        self.assertEqual(response.status_code, 200)

    def test_update_label(self):
        self.client.force_login(self.user)
        self.label = TaskLabels.objects.get(pk=1)
        self.assertNotEqual(self.label.name, self.test_label.get("name"))

        response = self.client.post(path=self.update_label_url,
                                    data=self.test_label)
        self.assertEqual(response.status_code, 302)

        self.label = TaskLabels.objects.get(pk=1)
        self.assertEqual(first=self.label.name,
                         second=self.test_label.get('name')
                         )


class TestDeleteLabel(TestCase):
    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        self.delete_label_url = reverse_lazy("label_delete", kwargs={"pk": 1})
        self.user = User.objects.get(pk=1)

    def test_open_delete_page_without_login(self):
        response = self.client.get(path=self.delete_label_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_delete_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.delete_label_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_delete_label(self):
        self.client.force_login(user=self.user)
        response = self.client.delete(path=self.delete_label_url)
        self.assertEqual(first=response.status_code, second=302)
        with self.assertRaises(TaskLabels.DoesNotExist):
            TaskLabels.objects.get(pk=1)
