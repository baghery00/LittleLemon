from django.test import TestCase
from restaurant.models import *
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        menu = Menu.objects.create(title='IceCream', price=23, inventory=100)
        self.assertEqual(menu, "IceCream : 23")