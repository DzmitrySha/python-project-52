from django.test import TestCase
from django.contrib.auth.models import User

from task_manager.models import TaskStatus


class UserTest(TestCase):
    # fixtures = ['test_data.json', 'moar_data.json']

    def setUp(self):
        User.objects.create(username="Kostya",
                            first_name="Konstantin",
                            last_name="Konstantinopolsky",
                            email="k_email@mail.com"
                            )
        User.objects.create(username="user1",
                            first_name="Fakename",
                            )

    def test_create_user(self):
        user = User.objects.get(username="Kostya")
        self.assertEqual(user.first_name, 'Konstantin')
        self.assertEqual(user.last_name, 'Konstantinopolsky')
        self.assertEqual(user.email, 'k_email@mail.com')

    def test_update_user(self):
        user = User.objects.get(username="Kostya")
        user.username = "Harpot"
        user.first_name = "Harry"
        user.last_name = "Potter"
        self.assertEqual(user.username, "Harpot")
        self.assertNotEqual(user.first_name, "Konstantin")
        self.assertEqual(user.last_name, "Potter")

    def test_delete_user(self):
        user1 = User.objects.get(username="user1")
        user1.delete()
        self.assertEqual(user1.id, None)
        self.assertEqual(user1.pk, None)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=2)


class TaskStatusTest(TestCase):
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


# import pytest
#
#
# @pytest.mark.django_db
# @pytest.fixture
# def user_admin():
#     user_admin = User(username="admin2",
#                       first_name="Admin2",
#                       last_name="Petrovich2"
#                       )
#     user_admin.save()
#     return user_admin
#
#
# @pytest.mark.django_db
# def test_user(user_admin):
#     assert user_admin.id == 1
#     assert user_admin.username == "admin2"
#     assert user_admin.first_name == "Admin2"
#     assert user_admin.last_name == "Petrovich2"
#
