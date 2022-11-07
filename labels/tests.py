from django.test import TestCase
from labels.models import Labels


class LabelsTest(TestCase):
    def setUp(self):
        Labels.objects.create(name="label 1",)
        Labels.objects.create(name="label 2",)

    def test_create_label(self):
        label_3 = Labels.objects.create(name="label created")
        self.assertEqual(label_3.name, "label created")

    def test_update_label(self):
        label_2 = Labels.objects.get(name="label 2")
        label_2.name = "another name"
        self.assertNotEqual(label_2.name, "label 2")

    def test_delete_label(self):
        label_1 = Labels.objects.get(name="label 1")
        label_1.delete()
        self.assertEqual(label_1.id, None)
        with self.assertRaises(Labels.DoesNotExist):
            Labels.objects.get(pk=8)
