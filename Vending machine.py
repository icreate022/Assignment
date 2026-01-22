class VendingItem:
    def __init__(self, name, price, stock):
        """Initialize a vending machine item."""
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, amount_paid):
        """Process a purchase attempt with the given amount paid."""
        if self.stock <= 0:
            print("Error: Out of stock.")
        elif amount_paid < self.price:
            print("Error: Insufficient funds.")
        else:
            self.stock -= 1
            print(f"Dispensing {self.name}.")
