from django.test import TestCase

# Create your tests here.
from katalog.models import CatalogItem


class KatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="cap", item_price=700, item_stock=4,
                                   description="new item", rating=9, item_url="google.com")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        cap = CatalogItem.objects.get(item_name="cap", item_price=700, item_stock=4,
                                      description="new item", rating=9, item_url="google.com")
        self.assertEqual(cap.item_name, "cap")
        self.assertEqual(cap.item_price, 700)
        self.assertEqual(cap.item_stock, 4)
        self.assertEqual(cap.description, "new item")
        self.assertEqual(cap.rating, 9)
        self.assertEqual(cap. item_url, "google.com")
