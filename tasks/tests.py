from django.test import TestCase
from tasks.models import Tasks


class TasksTest(TestCase):
    def setUp(self):
        Tasks.objects.create(name="task 1",)
        Tasks.objects.create(name="task 2",)

    def test_create_status(self):
        task_3 = Tasks.objects.create(name="task created")
        self.assertEqual(task_3.name, "task created")

    def test_update_status(self):
        task_2 = Tasks.objects.get(name="task 2")
        task_2.name = "another name"
        self.assertNotEqual(task_2.name, "task 2")

    def test_delete_status(self):
        task_1 = Tasks.objects.get(name="task 1")
        task_1.delete()
        self.assertEqual(task_1.id, None)
        with self.assertRaises(Tasks.DoesNotExist):
            Tasks.objects.get(pk=8)
