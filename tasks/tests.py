import os
import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from labels.models import TaskLabels
from statuses.models import TaskStatus
from tasks.models import Task
from task_manager.settings import FIXTURE_DIRS


class SetupTestTasks(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json']

    def setUp(self):
        self.tasks_url = reverse_lazy('tasks')
        self.login_url = reverse_lazy('login')
        self.create_task_url = reverse_lazy('task_create')
        self.update_task_url = reverse_lazy("task_update", kwargs={"pk": 1})
        self.delete_task_url = reverse_lazy("task_delete", kwargs={"pk": 1})
        self.detail_task_view_url = reverse_lazy('task_view', kwargs={"pk": 1})
        self.user = get_user_model().objects.get(pk=1)
        self.label = TaskLabels.objects.get(pk=1)
        self.status = TaskStatus.objects.get(pk=1)
        with open(os.path.join(FIXTURE_DIRS[0], "one_task.json")) as file:
            self.test_task = json.load(file)


class TestTaskList(SetupTestTasks):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

    def test_open_all_tasks_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.tasks_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_open_all_tasks_page_without_authorization(self):
        response = self.client.get(self.tasks_url)
        self.assertRedirects(response=response,
                             expected_url=self.login_url,
                             status_code=302, target_status_code=200)

    def test_open_detail_task_view_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.detail_task_view_url)
        self.assertEqual(first=response.status_code, second=200)


class TestCreateTask(SetupTestTasks):
    fixtures = ['users.json', 'statuses.json', 'labels.json']

    def test_open_create_status_page_without_login(self):
        response = self.client.get(self.create_task_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_create_status_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.create_task_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_create_task(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.create_task_url,
                                    data=self.test_task)
        self.assertRedirects(response=response, expected_url=self.tasks_url)
        self.assertEqual(first=response.status_code, second=302)

        self.task = Task.objects.get(pk=1)
        self.assertEqual(first=self.task.name,
                         second=self.test_task.get('name'))


class TestUpdateTask(SetupTestTasks):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

    def test_open_update_tasks_page_without_login(self):
        response = self.client.get(self.update_task_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_update_tasks_page_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.update_task_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_update_task(self):
        self.client.force_login(self.user)
        self.task = Task.objects.get(pk=1)
        self.assertNotEqual(self.task.name, self.test_task.get("name"))

        response = self.client.post(path=self.update_task_url,
                                    data=self.test_task)
        self.assertEqual(first=response.status_code, second=302)

        self.task = Task.objects.get(pk=1)
        self.assertEqual(first=self.task.name,
                         second=self.test_task.get('name')
                         )


class TestDeleteTask(SetupTestTasks):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

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
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=1)
