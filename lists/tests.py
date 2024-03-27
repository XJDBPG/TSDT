from django.test import TestCase

class SmokeTests(TestCase):
    def test_smoke(self):
        self.assertEqual(1+1, 3)
# Create your tests here.
