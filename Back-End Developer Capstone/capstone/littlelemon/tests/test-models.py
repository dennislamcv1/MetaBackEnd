from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_create_menu(self):
        # create a new menu object
        menu = Menu.objects.create(name='Breakfast', price=20, description='A selection of breakfast items')

        # check that the string representation of the object is as expected
        self.assertEqual(str(menu), 'Breakfast : A selection of breakfast items')

        # check that the name, price, and description fields are set correctly
        self.assertEqual(menu.name, 'Breakfast')
        self.assertEqual(menu.price, 20)
        self.assertEqual(menu.description, 'A selection of breakfast items')

        # check that the calculate_total_cost method works correctly
        self.assertEqual(menu.calculate_total_cost(), 30)