import policy_holder_class
import payment_processing_class 
from product_management_class import ProductManagement 
# Create instances of PolicyManagement, PaymentAndAccount, and ProductManagement
policy_management = policy_holder_class.PolicyManagement()
payment_and_account = payment_processing_class.PaymentAndAccount()
product_management = ProductManagement()

# Test policy holder management
policy_management.add_holder()
policy_management.add_holder()
policy_management.display_active_customers()

# Test payment processing
payment_and_account.receive_payment("John Doe", 100)
payment_and_account.issue_reminder("John Doe")
payment_and_account.reduce_balance("John Doe", 50)

# Test product management
product_management.subscribe_product("John Doe", "Life Insurance")
product_management.subscribe_product("John Doe", "Vehicle Insurance")

# Add details for an additional customer Neo Smith
policy_management.add_holder()  # Add Neo Smith
payment_and_account.receive_payment("Neo Smith", 150)
payment_and_account.issue_reminder("Neo Smith")
payment_and_account.reduce_balance("Neo Smith", 70)

# Test payment processing for Neo Smith
payment_and_account.receive_payment("Neo Smith", 150)
payment_and_account.issue_reminder("Neo Smith")
payment_and_account.reduce_balance("Neo Smith", 70)

#  Test product management for Neo Smith
product_management.add_product("Health Insurance")
product_management.add_product("Property Insurance")
product_management.subscribe_product("Neo Smith", "Health Insurance")
product_management.subscribe_product("Neo Smith", "Property Insurance")


# Display holders who have paid for products and their account balances
print("\nHolders with paid products and their account balances:")
print("-----------------------------------------------------")
for holder_name, balance in payment_and_account.holder_accounts.items():
    subscribed_products = product_management.subscribed_products.get(holder_name, [])
    if subscribed_products:
        print(f"Holder: {holder_name}")
        print(f"Subscribed Products: {', '.join(subscribed_products)}")
        print(f"Account Balance: ${balance}")
        print("----------------------------------------------")