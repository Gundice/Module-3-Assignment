class Policyholder:
    def __init__(self, name):
        self.name = name
        self.active = True

class PolicyManagement:
    def __init__(self):
        self.registered_holders = []
        self.suspended_holders = []

    def add_holder(self):
        name = input("Enter the policy holder's name: ")
        new_holder = Policyholder(name)
        self.registered_holders.append(new_holder)
        print(f"{name} successfully registered.")

    def suspend_holder(self):
        name = input("Enter the name of the holder you want to suspend: ")
        for holder in self.registered_holders:
            if holder.name == name:
                holder.active = False
                self.suspended_holders.append(holder)
                self.registered_holders.remove(holder)
                print(f"{name} successfully suspended.")
                return
        print("Customer not found.")

    def reactivate_holder(self):
        name = input("Enter the name of the customer you want to reactivate: ")
        for holder in self.suspended_holders:
            if holder.name == name:
                holder.active = True
                self.registered_holders.append(holder)
                self.suspended_holders.remove(holder)
                print(f"{name} successfully reactivated.")
                return
        print("Customer not found.")

    def display_active_customers(self):
        active_customers = [holder.name for holder in self.registered_holders if holder.active]
        print("Active Customers:")
        if active_customers:
            print("\n".join(active_customers))
        else:
            print("No active customers.")

# Test the policy management system
policy_management = PolicyManagement()
policy_management.add_holder()
policy_management.add_holder()
policy_management.display_active_customers()
policy_management.suspend_holder()
policy_management.display_active_customers()
policy_management.reactivate_holder()
policy_management.display_active_customers()
