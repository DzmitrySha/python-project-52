from django.test import TestCase
from users.models import User


class UsersTest(TestCase):
    fixtures = ['users.json']

    def test_create_user(self):
        user = User.objects.create(username="kep", first_name="Kevin",
                                   last_name="Phillips", email="kep@mail.com",
                                   )
        self.assertEqual(user.username, 'kep')
        self.assertEqual(user.first_name, 'Kevin')
        self.assertEqual(user.last_name, 'Phillips')
        self.assertEqual(user.email, 'kep@mail.com')

    def test_update_user(self):
        user1 = User.objects.get(pk=1)

        self.assertEqual(user1.username, "albert")
        self.assertEqual(user1.first_name, "Albert")
        self.assertEqual(user1.last_name, "Einstein")

        user1.username = "harry"
        user1.first_name = "Harry"
        user1.last_name = "Potter"

        self.assertEqual(user1.username, "harry")
        self.assertEqual(user1.first_name, "Harry")
        self.assertEqual(user1.last_name, "Potter")

    def test_delete_user(self):
        user = User.objects.get(pk=2)
        user.delete()
        self.assertEqual(user.id, None)
        self.assertEqual(user.pk, None)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=2)
