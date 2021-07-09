from django.http import response
from django.test import TestCase
from django.urls import reverse


class PlacesListTestCase(TestCase):
    def test_open_list_success(self):
        url = reverse('places-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
