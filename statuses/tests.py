from django.test import TestCase
from statuses.models import TaskStatus


class StatusesTest(TestCase):
    def setUp(self):
        TaskStatus.objects.create(name="status 1",)
        TaskStatus.objects.create(name="status 2",)

    def test_create_status(self):
        status_3 = TaskStatus.objects.create(name="status created")
        self.assertEqual(status_3.name, "status created")

    def test_update_status(self):
        status_2 = TaskStatus.objects.get(name="status 2")
        status_2.name = "another name"
        self.assertNotEqual(status_2.name, "status 2")

    def test_delete_status(self):
        status_1 = TaskStatus.objects.get(name="status 1")
        status_1.delete()
        self.assertEqual(status_1.id, None)
        with self.assertRaises(TaskStatus.DoesNotExist):
            TaskStatus.objects.get(pk=8)
