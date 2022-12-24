import os
import json

from django.test import TestCase
from django.urls import reverse_lazy

from labels.models import Label
from statuses.models import TaskStatus
from tasks.models import Tasks
from users.models import User
from task_manager.settings import FIXTURE_DIRS


class TestTaskList(TestCase):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

    def setUp(self):
        self.one_task_view_url = reverse_lazy('task_view', kwargs={"pk": 1})
        self.tasks_url = reverse_lazy('tasks')

    def test_open_tasks_page(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, 200)

    def test_open_one_task_view_page(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(self.one_task_view_url)
        self.assertEqual(response.status_code, 200)


class TestCreateTask(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json']

    def setUp(self):
        self.tasks_url = reverse_lazy('tasks')
        self.create_task_url = reverse_lazy('task_create')
        self.user = User.objects.get(pk=1)
        self.status = TaskStatus.objects.get(pk=1)
        self.label = Label.objects.get(pk=1)
        self.test_task = json.load(
            open(os.path.join(FIXTURE_DIRS[0], "one_task.json")))

    def test_open_create_status_page_without_login(self):
        response = self.client.get(self.create_task_url)
        self.assertEqual(response.status_code, 302)

    def test_open_create_status_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.create_task_url)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.create_task_url,
                                    data=self.test_task)
        self.assertRedirects(response=response, expected_url=self.tasks_url)
        self.assertEqual(response.status_code, 302)

        self.task = Tasks.objects.get(pk=1)
        self.assertEqual(first=self.task.name,
                         second=self.test_task.get('name'))


class TestUpdateTask(TestCase):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

    def setUp(self):
        self.update_task_url = reverse_lazy("task_update", kwargs={"pk": 1})
        self.user = User.objects.get(pk=1)
        self.test_task = json.load(
            open(os.path.join(FIXTURE_DIRS[0], "one_task.json")))

    def test_open_update_tasks_page_without_login(self):
        response = self.client.get(self.update_task_url)
        self.assertEqual(response.status_code, 302)

    def test_open_update_tasks_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.update_task_url)
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        self.client.force_login(self.user)
        self.task = Tasks.objects.get(pk=1)
        self.assertNotEqual(self.task.name, self.test_task.get("name"))

        response = self.client.post(path=self.update_task_url,
                                    data=self.test_task)
        self.assertEqual(response.status_code, 302)

        self.task = Tasks.objects.get(pk=1)
        self.assertEqual(first=self.task.name,
                         second=self.test_task.get('name')
                         )


class TestDeleteTask(TestCase):
    fixtures = ['users.json', 'tasks.json', 'statuses.json']

    def setUp(self):
        self.delete_task_url = reverse_lazy("task_delete", kwargs={"pk": 1})
        self.user = User.objects.get(pk=1)

    def test_open_delete_page_without_login(self):
        response = self.client.get(path=self.delete_task_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_delete_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.delete_task_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_delete_task(self):
        self.client.force_login(user=self.user)
        response = self.client.delete(path=self.delete_task_url)
        self.assertEqual(first=response.status_code, second=302)
        with self.assertRaises(Tasks.DoesNotExist):
            Tasks.objects.get(pk=1)
