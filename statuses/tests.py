import json
from django.test import TestCase
from statuses.models import TaskStatus


class StatusesTest(TestCase):
    fixtures = ['statuses.json']

    def test_create_status(self):
        data_status = json.load(open("fixtures/status.json"))
        status = TaskStatus.objects.create(**data_status)
        self.assertEqual(status.name, data_status.get("name"))

    def test_update_status(self):
        data_status = json.load(open("fixtures/status.json"))

        status = TaskStatus.objects.get(pk=2)
        self.assertNotEqual(status.name, data_status.get("name"))

        status.name = data_status.get("name")
        self.assertEqual(status.name, data_status.get("name"))

    def test_delete_status(self):
        status = TaskStatus.objects.get(pk=1)
        status.delete()
        self.assertEqual(status.id, None)
        with self.assertRaises(TaskStatus.DoesNotExist):
            TaskStatus.objects.get(pk=1)
