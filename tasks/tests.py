from django.contrib.auth.models import User
from django.test import TestCase

from statuses.models import TaskStatus
from tasks.models import Tasks


class TasksTest(TestCase):
    def setUp(self):
        author = User.objects.create(username='Harry')
        status = TaskStatus.objects.create(name='Done')
        Tasks.objects.create(name="task 1", author=author, status=status)
        Tasks.objects.create(name="task 2", author=author, status=status)

    def test_create_status(self):
        author = User.objects.create(username='Harry2')
        status = TaskStatus.objects.create(name='Done2')
        task_3 = Tasks.objects.create(name="task created",
                                      author=author, status=status)
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
