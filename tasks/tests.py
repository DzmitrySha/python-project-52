import json
from django.test import TestCase
from tasks.models import Tasks


class TasksTest(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def test_create_task(self):
        data_task = json.load(open("fixtures/one_task.json"))
        task = Tasks.objects.create(**data_task)
        self.assertEqual(task.name, data_task.get("name"))
        self.assertEqual(task.author_id, data_task.get("author_id"))
        self.assertEqual(task.executor_id, data_task.get("executor_id"))

    def test_update_task(self):
        data_task = json.load(open("fixtures/one_task.json"))
        task = Tasks.objects.get(pk=1)

        new_name = data_task.get("name")
        new_author_id = data_task.get("author_id")
        new_executor_id = data_task.get("executor_id")
        new_status_id = data_task.get("status_id")
        new_description = data_task.get("description")

        self.assertNotEqual(task.name, new_name)
        self.assertNotEqual(task.author_id, new_author_id)
        self.assertNotEqual(task.executor_id, new_executor_id)
        self.assertNotEqual(task.status_id, new_status_id)
        self.assertNotEqual(task.description, new_description)

        task.name = new_name
        task.author_id = new_author_id
        task.executor_id = new_executor_id
        task.status_id = new_status_id
        task.description = new_description

        self.assertEqual(task.name, new_name)
        self.assertEqual(task.author_id, new_author_id)
        self.assertEqual(task.executor_id, new_executor_id)
        self.assertEqual(task.status_id, new_status_id)
        self.assertEqual(task.description, new_description)

    def test_delete_task(self):
        task = Tasks.objects.get(pk=2)
        task.delete()
        self.assertEqual(task.id, None)
        with self.assertRaises(Tasks.DoesNotExist):
            Tasks.objects.get(pk=2)
