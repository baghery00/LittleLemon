import random
from django.test import TestCase
from restaurant.models import *
from restaurant.serializers import *
from restaurant.views import *
from django.test import Client

class MenuViewTest(TestCase):
    def setUp(self):
        for i in range(0,5):
            menu = Menu.objects.create(title=f'menu{i}', price=random.randint(0,120), inventory=30)
            menu.save()
    def test_getall(self):
        client = Client()
        client.login({'username':'admin', 'password':'123'})
        res = client.get("/restaurant/menu/", headers={"accept": "application/json"})        # res = MenuItemView(req)
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(serializer.data , res.json())
