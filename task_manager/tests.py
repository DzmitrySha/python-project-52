# import pytest
from django.test import TestCase
from django.contrib.auth.models import User

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


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Kostya",
                            first_name="Konstantin",
                            last_name="Konstantinopolsky",
                            email="k_email@mail.com"
                            )

    def test_create_user(self):
        user = User.objects.get(username="Kostya")
        self.assertEqual(user.first_name, 'Konstantin')
        self.assertEqual(user.last_name, 'Konstantinopolsky')
        self.assertEqual(user.email, 'k_email@mail.com')
