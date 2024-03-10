from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .views import index

class TestIndexView(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Django! From Shovan")
