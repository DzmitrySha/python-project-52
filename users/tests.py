import os
import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.settings import FIXTURE_DIRS
from users.forms import UserCreationFormCustom


class SetupTestUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.create_url = reverse_lazy('create')
        self.update_url = reverse_lazy('update', kwargs={"pk": 1})
        self.delete_url = reverse_lazy("delete", kwargs={"pk": 1})
        self.login_url = reverse_lazy('login')
        self.users_url = reverse_lazy('users')
        self.users = get_user_model().objects.all()
        self.user = get_user_model().objects.get(pk=1)
        self.user2 = get_user_model().objects.get(pk=2)
        self.test_user = json.load(
            open(os.path.join(FIXTURE_DIRS[0], "one_user.json")))


class TestCreateUser(SetupTestUser):

    def test_open_create_page(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(path=self.create_url, data=self.test_user)
        self.assertEqual(response.status_code, 302)
        self.user = get_user_model().objects.get(pk=4)
        self.assertEqual(first=self.user.username,
                         second=self.test_user.get('username'))

        self.assertEqual(first=self.user.first_name,
                         second=self.test_user.get('first_name'))
        self.assertEqual(first=self.user.last_name,
                         second=self.test_user.get('last_name'))


class TestUserCreationForm(SetupTestUser):

    def test_user_create_form_with_data(self):
        user_form = UserCreationFormCustom(data=self.test_user)
        self.assertTrue(user_form.is_valid())
        self.assertEqual(len(user_form.errors), 0)

    def test_user_creation_form_with_no_data(self):
        user_form = UserCreationFormCustom(data={})
        self.assertFalse(user_form.is_valid())
        self.assertEqual(len(user_form.errors), 5)


class TestUpdateUser(SetupTestUser):

    def test_open_update_page(self):
        # with no login
        response = self.client.get(self.update_url)
        self.assertRedirects(response, self.login_url, 302, 200)
        # with login
        self.client.force_login(self.user)
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        self.client.force_login(self.user)
        self.assertNotEqual(self.user.username, self.test_user.get("username"))
        response = self.client.post(self.update_url, data=self.test_user)
        self.assertEqual(response.status_code, 302)
        self.user = get_user_model().objects.get(pk=1)
        self.assertEqual(self.user.username, self.test_user.get("username"))

    def test_update_other_user(self):
        self.client.force_login(self.user2)
        response = self.client.post(self.update_url, data=self.test_user)
        self.assertRedirects(response, self.users_url, 302, 200)


class TestDeleteUser(SetupTestUser):

    def test_open_delete_page(self):
        # with no login
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.login_url, 302)
        # with login (self delete user)
        self.client.force_login(self.user)
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        # with login (delete other user)
        self.client.force_login(self.user2)
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        self.client.force_login(self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.users.count(), 2)
        with self.assertRaises(get_user_model().DoesNotExist):
            get_user_model().objects.get(pk=1)

    def test_delete_other_user(self):
        self.client.force_login(self.user2)
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.users.count(), 3)
