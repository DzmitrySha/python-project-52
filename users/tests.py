import json
from django.test import TestCase
from django.urls import reverse_lazy
from users.models import User


class UsersTest(TestCase):
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


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse_lazy('create')
        self.user = {
            'username': 'helena',
            'first_name': 'Helen',
            'last_name': 'Barrett',
            'password': 'BarHe818',
            'password2': 'BarHe818'
        }
        self.user_short_password = {
            'username': 'helena',
            'first_name': 'Helen',
            'last_name': 'Barrett',
            'password': '111',
            'password2': '111'
        }
        return super().setUp()


class RegisterUserTest(BaseTest):

    def test_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/form.html')

    def test_get_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(
            self.register_url, self.user, format='text/html'
        )
        self.assertEqual(response.status_code, 200)  # 302

    def test_cant_register_user_with_short_password(self):
        response = self.client.post(
            self.register_url, self.user_short_password, format='text/html'
        )
        self.assertEqual(response.status_code, 200)  # 400
