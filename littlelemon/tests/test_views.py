# tests/test_views.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(Title="Pizza", Price=9.99)
        self.menu2 = Menu.objects.create(Title="Burger", Price=5.99)
        self.menu3 = Menu.objects.create(Title="Pasta", Price=7.99)

    def test_getall(self):
        response = self.client.get('/menu/')  # Adjust endpoint if needed
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
