# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 6/28/2022
# Description: tester for lemondade
#


import unittest

from LemonadeStand import LemonadeStand, SalesForDay, InvalidSalesItemError, MenuItem

class Test_LemonadeStand(unittest.TestCase):

    def test_1(self):
        """Test get_name()"""
        name = LemonadeStand("Lemons R Us")
        self.assertEqual(name.get_name(), 'Lemons R Us')

    def test_2(self):
        """Tests wholesale cost and selling price"""
        sales = MenuItem('lemonade', .5, 1.5)
        self.assertAlmostEqual(sales.get_wholesale_cost(), .5)
        self.assertAlmostEqual(sales.get_selling_price(), 1.5)

    def test_3(self):
        """Tests get_sales_dictionary"""
        item1 = MenuItem('lemonade', 0.5, 1.5)
        self.assertEqual(item1.get_name(), 'lemonade')

    def test_4(self):
        """Tests item2 """
        item1 = MenuItem('nori', 0.6, 0.8)
        self.assertTrue(item1.get_name() == 'nori')

    def test_5(self):
        """tests item2"""
        item1 = MenuItem('lemonade', 0.5, 1.5)
        self.assertTrue(item1.get_name() == 'lemonade')




if __name__ == '__main__':
    unittest.main()
