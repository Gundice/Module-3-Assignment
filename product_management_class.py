class ProductManagement:
    def __init__(self):
        self.products = ['Life Insurance', 'Vehicle Insurance']
        self.subscribed_products = {}

    def add_product(self, product_name):
        if product_name not in self.products:
            self.products.append(product_name)
            print(f"{product_name} added to the product list.")
        else:
            print(f"{product_name} already exists in the product list.")

    def remove_product(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)
            print(f"{product_name} removed from the product list.")
        else:
            print(f"{product_name} does not exist in the product list.")

    def subscribe_product(self, holder_name, product_name):
        if product_name in self.products:
            if holder_name in self.subscribed_products:
                if product_name in self.subscribed_products[holder_name]:
                    print(f"{holder_name} is already subscribed to {product_name}.")
                else:
                    self.subscribed_products[holder_name].append(product_name)
                    print(f"{holder_name} subscribed to {product_name}.")
            else:
                self.subscribed_products[holder_name] = [product_name]
                print(f"{holder_name} subscribed to {product_name}.")
        else:
            print(f"{product_name} does not exist in the product list.")

    def unsubscribe_product(self, holder_name, product_name):
        if holder_name in self.subscribed_products:
            if product_name in self.subscribed_products[holder_name]:
                self.subscribed_products[holder_name].remove(product_name)
                print(f"{holder_name} unsubscribed from {product_name}.")
            else:
                print(f"{holder_name} is not subscribed to {product_name}.")
        else:
            print(f"{holder_name} is not subscribed to any products.")
product_management = ProductManagement()

# Test adding a product
print("Adding products:")
product_management.add_product("Home Insurance")
product_management.add_product("Health Insurance")
product_management.add_product("Life Insurance")  # Already exists
print()

# Test removing a product
print("Removing products:")
product_management.remove_product("Health Insurance")
product_management.remove_product("Auto Insurance")  # Does not exist
print()

# Test subscribing to a product
print("Subscribing to products:")
product_management.subscribe_product("John Doe", "Home Insurance")
product_management.subscribe_product("John Doe", "Life Insurance")  # Already subscribed
product_management.subscribe_product("Jane Smith", "Auto Insurance")  # Does not exist
print()

# Test unsubscribing from a product
print("Unsubscribing from products:")
product_management.unsubscribe_product("John Doe", "Home Insurance")
product_management.unsubscribe_product("John Doe", "Auto Insurance")  # Not subscribed
product_management.unsubscribe_product("Jane Smith", "Life Insurance")  # Not subscribed
print()

# Display the products and subscribed products
print("Current Products:", product_management.products)
print("Subscribed Products:", product_management.subscribed_products)
