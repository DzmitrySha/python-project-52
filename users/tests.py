import json
from django.test import TestCase
from users.models import User


class UsersTest(TestCase):
    fixtures = ['users.json']

    def test_create_user(self):
        user_data = json.load(open("fixtures/user.json"))
        user = User.objects.create(**user_data)

        self.assertEqual(user.username, user_data.get('username'))
        self.assertEqual(user.first_name, user_data.get('first_name'))
        self.assertEqual(user.last_name, user_data.get('last_name'))
        self.assertEqual(user.email, user_data.get('email'))

    def test_update_user(self):
        user_data = json.load(open("fixtures/user.json"))
        user1 = User.objects.get(pk=1)

        self.assertNotEqual(user1.username, user_data.get('username'))
        self.assertNotEqual(user1.first_name,  user_data.get('first_name'))
        self.assertNotEqual(user1.last_name, user_data.get('last_name'))

        user1.username = user_data.get('username')
        user1.first_name = user_data.get('first_name')
        user1.last_name = user_data.get('last_name')
        user1.email = user_data.get('email')

        self.assertEqual(user1.username, user_data.get('username'))
        self.assertEqual(user1.first_name,  user_data.get('first_name'))
        self.assertEqual(user1.last_name, user_data.get('last_name'))
        self.assertEqual(user1.last_name, user_data.get('email'))

    def test_delete_user(self):
        user = User.objects.get(pk=2)
        user.delete()
        self.assertEqual(user.id, None)
        self.assertEqual(user.pk, None)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=2)
