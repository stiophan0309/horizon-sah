from django.test import TestCase
from .models import Work

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Work(name='An artwork')
        self.assertEqual(str(test_name), 'An artwork')
