# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 6/28/2022
# Description: Returns lemonade stand sales and profits
#



class MenuItem:
    """class for getting menu information"""
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """get method for item name"""
        return self._name

    def get_wholesale_cost(self):
        """get method for wholesale cost of item"""
        return self._wholesale_cost

    def get_selling_price(self):
        """get method for selling price of item"""
        return self._selling_price


class SalesForDay:
    """class to record daily sales"""

    def __init__(self, number_of_days, sales_dictionary):
        self._number_of_days = number_of_days
        self._sales_dictionary = sales_dictionary

    def get_day(self):
        """get method for day"""
        return self._number_of_days

    def get_sales_dictionary(self):
        """get method for sales dictionary"""
        return self._sales_dictionary

class InvalidSalesItemError(Exception):
    pass

class LemonadeStand:
    """class for stand and other attributes"""
    def __init__(self, stand_name):
        self._stand_name = stand_name
        self._current_day = 0
        self._menu = {}
        self._daily_sales = []

    def get_name(self):
        """get method for stand name"""
        return self._stand_name

    def add_menu_item(self, menu_item):
        """adds item to stand menu"""
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dictionary):
        """checks to see if it sold is on menu"""
        sales_for_today = SalesForDay(self._current_day, sales_dictionary)
        self._daily_sales.append(sales_for_today)
        self._current_day += 1
        try:
            for item, value in sales_dictionary.items():
                if item not in self._menu.keys():
                    raise InvalidSalesItemError

        except InvalidSalesItemError:
            print("Sales item must be in the menu!")

    def get_sales_dict_for_day(self, day):
        """daily sales dictionary"""
        for item in self._daily_sales:
            if item.get_day() == day:
                return item.get_sales_dictionary()

    def total_sales_for_menu_item(self, menu_item_name):
        """calculates total items sold"""
        total_sales = 0

        for item in self._daily_sales:
            for item, value in item.get_sales_dictionary().items():
                if item.lower() == menu_item_name.lower():
                    total_sales += value

        return total_sales

    def total_profit_for_menu_item(self, menu_item_name):
        """calculates profit per item"""
        total_sales_of_item = self.total_sales_for_menu_item(menu_item_name)

        menu_item = self._menu.get(menu_item_name)

        total_profit = total_sales_of_item * menu_item.get_selling_price() - total_sales_of_item * menu_item.get_wholesale_cost()

        return total_profit

    def total_profit_for_stand(self):
        """calculates stand total profit"""
        total_profit = 0

        for name, menu_item in self._menu.items():
            total_sales_of_item = self.total_sales_for_menu_item(name)
            profit = total_sales_of_item * menu_item.get_selling_price() - total_sales_of_item * menu_item.get_wholesale_cost()
            total_profit += profit

        return total_profit





def main():
    stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand called 'Lemons R Us'
    item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

    # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
    day_0_sales = {'lemonade': 5, 'cookie': 2}
    day_1_sales = {'lemonad': 5, 'cookie': 2}
    stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    #stand.enter_sales_for_today(day_1_sales) # test for exception class
    print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")  # print the total profit for lemonade so far

if __name__ == "__main__":
    main()