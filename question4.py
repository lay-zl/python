"""
Below is the item class. unique_id identifies each item. The task is to build a class for shopping Cart.
 Cart can have any number of items, cart must have the facility to add items, remove items 
 and calculate the total price of the cart. 
"""

"""

15
"""

class Item:
    def __init__(self, unique_id, name, price):
        self.unique_id = unique_id
        self.name = name
        self.price = price


class Cart:
    def __init__(...):
        pass

    def add_item(...):
        pass

    def remove_item(...):
        pass

    def get_total(...):
        pass


if __name__ == '__main__':
    book = Item('001', 'Book', 10)
    pen = Item('002', 'Pen', 5)
    
    cart1 = Cart()
    cart1.add_item(book)
    cart1.add_item(book)
    cart1.add_item(pen)
    cart1.add_item(pen)
    cart1.remove_item(pen)
    assert cart1.get_total() == 25

    cart2 = Cart()
    cart2.add_item(book)
    cart2.add_item(pen)
    assert cart2.get_total() == 15