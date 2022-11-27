from django.test import TestCase
from statuses.models import TaskStatus


class StatusesTest(TestCase):
    fixtures = ['statuses.json']

    def test_create_status(self):
        status = TaskStatus.objects.create(name="status created")
        self.assertEqual(status.name, "status created")

    def test_update_status(self):
        status = TaskStatus.objects.get(pk=2)
        status.name = "another name"
        self.assertNotEqual(status.name, "status 2")

    def test_delete_status(self):
        status = TaskStatus.objects.get(pk=1)
        status.delete()
        self.assertEqual(status.id, None)
        with self.assertRaises(TaskStatus.DoesNotExist):
            TaskStatus.objects.get(pk=8)
