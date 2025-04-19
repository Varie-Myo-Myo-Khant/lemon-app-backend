from django.test import TestCase
from restaurant.models import Menu
class MenuItemTest(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(Title="IceCream",Price=80)
        self.assertEqual(item,"IceCream:80")