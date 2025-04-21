from django.test import TestCase
from .models import MyModel

class MyModelTest(TestCase):
    def test_model_creation(self):
        obj = MyModel.objects.create(name="Test Object")
        self.assertEqual(obj.name, "Test Object")
        self.assertTrue(MyModel.objects.exists())