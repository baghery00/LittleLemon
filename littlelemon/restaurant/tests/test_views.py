import random
from django.test import TestCase
from restaurant.models import *

class MenuViewTest(TestCase):
    def setUp(self):
        for i in range(0,5):
            menu = Menu.objects.create(title=f'menu{i}', price=random.randint(0,120), inventory=30)
            menu.save()
    def test_getall(self):
        pass
