from collections import defaultdict


class InventoryManager:
    """
    Inventory tracking and low-stock alert system.
    """

    def __init__(self):
        self.inventory = defaultdict(dict)

    def add_product(
        self,
        sku,
        name,
        quantity,
        reorder_level
    ):
        """
        Add or update a product in inventory.
        """

        self.inventory[sku] = {
            "name": name,
            "quantity": quantity,
            "reorder_level": reorder_level
        }

    def update_stock(self, sku, quantity_change):
        """
        Increase or decrease stock quantity.
        """

        if sku not in self.inventory:
            return {
                "success": False,
                "message": "Product not found"
            }

        self.inventory[sku]["quantity"] += quantity_change

        return {
            "success": True,
            "updated_product": self.inventory[sku]
        }

    def get_low_stock_products(self):
        """
        Return all products below reorder level.
        """

        low_stock = []

        for sku, product in self.inventory.items():
            if (
                product["quantity"]
                <= product["reorder_level"]
            ):
                low_stock.append({
                    "sku": sku,
                    "name": product["name"],
                    "quantity": product["quantity"]
                })

        return low_stock

    def generate_inventory_report(self):
        """
        Generate inventory summary report.
        """

        total_products = len(self.inventory)

        total_items = sum(
            product["quantity"]
            for product in self.inventory.values()
        )

        return {
            "total_products": total_products,
            "total_items": total_items,
            "low_stock_products": (
                self.get_low_stock_products()
            )
        }


# Example usage
manager = InventoryManager()

manager.add_product(
    sku="KB001",
    name="Mechanical Keyboard",
    quantity=15,
    reorder_level=10
)

manager.add_product(
    sku="MS002",
    name="Wireless Mouse",
    quantity=5,
    reorder_level=8
)

manager.update_stock(
    sku="KB001",
    quantity_change=-7
)

report = manager.generate_inventory_report()