from django.test import TestCase
from django.contrib.auth.models import User


class UsersTest(TestCase):
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
