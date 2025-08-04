class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  # list of (item_name, quantity, price)
    
    def add_item(self, name, quantity, price):
        self.items.append((name, quantity, price))
    
    def calculate_total(self):
        total = 0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def apply_discount(self, total):
        if total >= 500:
            return total * 0.9  # 10% discount
        return total
    
    def summary(self):
        print(f"\nOrder for: {self.customer_name}")
        for name, qty, price in self.items:
            print(f"{qty} x {name} @ R{price} each")
        total = self.calculate_total()
        discounted_total = self.apply_discount(total)
        print(f"Total: R{total}")
        if discounted_total < total:
            print("Discount applied!")
        print(f"Final Total: R{discounted_total}")

# Example usage
order1 = Order("Khumo")
order1.add_item("Laptop Bag", 1, 350)
order1.add_item("USB-C Hub", 2, 100)
order1.add_item("Notebook", 3, 50)

order1.summary()
