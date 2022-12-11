import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from users.models import User


class BaseUserTest(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.users_url = reverse('users')
        self.create_url = reverse('create')
        self.update_url = reverse('update', kwargs={"pk": 1})
        self.delete_url = reverse('delete', kwargs={"pk": 1})
        self.user = get_user_model().objects.get(pk=1)
        self.correct_user = json.load(
            open("fixtures/reg_users.json"))['correct_user']
        self.wrong_user = json.load(
            open("fixtures/reg_users.json"))['wrong_user']


class TestLoadPages(BaseUserTest):

    def test_load_pages(self):
        response_login = self.client.get(path=self.login_url)
        self.assertEqual(first=response_login.status_code, second=200)
        self.assertTemplateUsed(response_login, 'users/form.html')

        response_logout = self.client.post(path=self.logout_url)
        self.assertEqual(first=response_logout.status_code, second=302)

        response_users = self.client.get(path=self.users_url)
        self.assertEqual(first=response_users.status_code, second=200)
        self.assertTemplateUsed(response_users, 'users/users.html')

        response_create = self.client.get(path=self.create_url)
        self.assertEqual(first=response_create.status_code, second=200)
        self.assertTemplateUsed(response_create, 'users/form.html')

        response_update = self.client.get(path=self.update_url)
        self.assertEqual(first=response_update.status_code, second=302)

        response_delete = self.client.get(path=self.delete_url)
        self.assertEqual(first=response_delete.status_code, second=302)


class TestUser(BaseUserTest):

    def test_create_user(self):

        response = self.client.post(path=self.create_url,
                                    data=self.correct_user
                                    )
        self.assertEqual(first=response.status_code, second=200)
        self.assertEqual(get_user_model().objects.count(), 3)
        self.assertEqual(get_user_model().objects.get(pk=2).username, 'richclark')

    def test_get_users(self):
        response = self.client.get(path=self.users_url)
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(path=self.create_url,
                                    data=self.correct_user
                                    )
        self.assertEqual(response.status_code, 200)  # 302

    def test_cant_register_user_with_short_password(self):
        response = self.client.post(path=self.create_url, data=self.wrong_user)
        self.assertEqual(response.status_code, 200)  # 400


class UsersTestOld(TestCase):
    fixtures = ['users.json']

    def test_create_user(self):
        user_data = json.load(open("fixtures/one_user.json"))
        user = User.objects.create(**user_data)

        self.assertEqual(user.username, user_data.get('username'))
        self.assertEqual(user.first_name, user_data.get('first_name'))
        self.assertEqual(user.last_name, user_data.get('last_name'))

    def test_update_user(self):
        user_data = json.load(open("fixtures/one_user.json"))
        user1 = User.objects.get(pk=1)

        self.assertNotEqual(user1.username, user_data.get('username'))
        self.assertNotEqual(user1.first_name, user_data.get('first_name'))
        self.assertNotEqual(user1.last_name, user_data.get('last_name'))

        user1.username = user_data.get('username')
        user1.first_name = user_data.get('first_name')
        user1.last_name = user_data.get('last_name')

        self.assertEqual(user1.username, user_data.get('username'))
        self.assertEqual(user1.first_name, user_data.get('first_name'))
        self.assertEqual(user1.last_name, user_data.get('last_name'))

    def test_delete_user(self):
        user = User.objects.get(pk=2)
        user.delete()
        self.assertEqual(user.id, None)
        self.assertEqual(user.pk, None)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=2)
