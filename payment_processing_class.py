class PaymentAndAccount:
    def __init__(self):
        self.holder_accounts = {}

    def receive_payment(self, holder_name, amount):
        if holder_name in self.holder_accounts:
            self.holder_accounts[holder_name] += amount
        else:
            self.holder_accounts[holder_name] = amount
        print(f"Received payment of ${amount} from {holder_name}.")

    def issue_reminder(self, holder_name):
        print(f"Reminder: Please make a payment, {holder_name}.")

    def reduce_balance(self, holder_name, amount):
        if holder_name in self.holder_accounts:
            self.holder_accounts[holder_name] -= amount
            print(f"{amount} deducted from {holder_name}'s account.")
        else:
            print(f"No account found for {holder_name}.")


