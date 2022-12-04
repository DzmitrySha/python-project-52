import json

from django.test import TestCase
from labels.models import Label


class LabelsTest(TestCase):
    fixtures = ['labels.json']

    def test_create_label(self):
        data_label = json.load(open("fixtures/label.json"))
        label = Label.objects.create(**data_label)
        self.assertEqual(label.name, data_label.get("name"))

    def test_update_label(self):
        data_label = json.load(open("fixtures/label.json"))

        label = Label.objects.get(pk=2)
        self.assertNotEqual(label.name, data_label.get("name"))

        label.name = data_label.get("name")
        self.assertEqual(label.name, data_label.get("name"))

    def test_delete_label(self):
        label = Label.objects.get(pk=1)
        label.delete()
        self.assertEqual(label.id, None)
        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=1)
