class Item:
    """
    Represents an item in the shopping cart
    attributes: name, price
    """
    def __init__(self, name, price):
        """
        Initialize the attributes
        """
        self.name = name
        self.price = price
    
    def __str__(self):
        """
        Return the name and price of the item in a human-readable format
        """
        return f'{self.name} : ${self.price:.2f}'

class ShoppingCart:
    """
    Represents the shopping cart
    attributes: a list to store items, total price of the items
    """
    def __init__(self):
        """
        Initialize the attributes
        """
        self.items = []
        self.total = 0.0
    
    def __str__(self):
        """
        Return the number of items in a human-readable format
        """
        return  f'There are {len(self.items)} items in your Shoppinhg Cart.'
    
    def __add__ (self, other):
        """
        Operator Overloading

        Overloads the "+" operator
        """
        self.total += other
    
    def add_item(self, item):
        """
        Method to add an item to the shopping cart
        """
        self.items.append(item)
        self.total += item.price
        print(f"Added {item.name} to the shopping cart.")
    
    def remove_item(self, item):
        """
        Method to remove an item from the shopping cart
        """        
        if item in self.items:          
            self.items.remove(item)
            self.total -= item.price  
            print(f"Removed {item.name} from the shopping cart.")
        else:
            print(f"{item.name} not found in the shopping cart.")
  
    def view_cart(self):
        """
        Method to view the items in the shopping cart
        """
        if len(self.items) > 0:
            print("Items in the shopping cart:")
            for item in self.items:
                print(f"- {item}")
            print(f"Total: ${self.total:.2f}")
        else:
            print("No items in the shopping cart.")

cart1 = ShoppingCart()
cart2 = ShoppingCart()

item1 = Item("Apple", 2.00)
item2 = Item("Pencil", 5.00)
item3 = Item("MacBook", 2000.00)
item4 = Item("Ipad", 1200.00)

cart1.add_item(item1)
cart1.add_item(item2)
cart2.add_item(item3)
cart2.add_item(item4)

cart1.view_cart()
cart2.view_cart()

cart1.remove_item(item2)
cart2 + 0.0625*cart2.total

cart1.view_cart()
cart2.view_cart()