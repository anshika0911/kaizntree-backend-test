from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Data, Categories, Items

class ModelTestCase(TestCase):
    def setUp(self):
        # Create some test data for models
        self.category = Categories.objects.create(name='Test Category')
        self.item = Items.objects.create(sku='TEST123', name='Test Item', category_id=self.category, in_stock=10, available_stock=5)

    def test_data_model(self):
        data = Data.objects.create(name='Test Data', description='Test Description')
        self.assertEqual(data.name, 'Test Data')
        self.assertEqual(data.description, 'Test Description')

    def test_categories_model(self):
        category = Categories.objects.get(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

    def test_items_model(self):
        item = Items.objects.get(sku='TEST123')
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.category_id.name, 'Test Category')
        self.assertEqual(item.in_stock, 10)
        self.assertEqual(item.available_stock, 5)

class APITestCase(TestCase):
    def setUp(self):
        # Create some test data for API endpoints
        self.client = APIClient()
        self.category = Categories.objects.create(name='Test Category')
        self.item = Items.objects.create(sku='TEST123', name='Test Item', category_id=self.category, in_stock=10, available_stock=5)

    def test_items_list_api(self):
        url = reverse('items-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Assuming only one item in the database
        self.assertEqual(response.data[0]['sku'], 'TEST123')

    def test_item_detail_api(self):
        url = reverse('item-detail', kwargs={'pk': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Item')

    # Add more test cases for other API endpoints as needed

