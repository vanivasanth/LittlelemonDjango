from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu
from .serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create some test Menu items
        self.menu1 = Menu.objects.create(title="Pizza", price=12.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Pasta", price=9.99, inventory=15)
        self.menu3 = Menu.objects.create(title="Salad", price=7.49, inventory=20)
        self.client = APIClient()

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')  # Adjust the URL as needed
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)