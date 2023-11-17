class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.user_authenticated = False
        self.transaction_history = []  # Initialize an empty list for transaction history

    def authenticate(self, user_id, pin):
        if user_id == "1234" and pin == "5678":
            self.user_authenticated = True
            return True
        else:
            print("Invalid user ID or PIN. Authentication failed.")
            return False

    def display_balance(self):
        if self.user_authenticated:
            print(f"Your account balance is ${self.balance:.2f}")
        else:
            print("Please authenticate first.")

    def withdraw(self, amount):
        if self.user_authenticated:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount:.2f}")
                print(f"Withdrew ${amount:.2f}.")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("Please authenticate first.")

    def deposit(self, amount):
        if self.user_authenticated:
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited ${amount:.2f}")
                print(f"Deposited ${amount:.2f}.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Please authenticate first.")

    def transfer(self, recipient_account, amount):
        if self.user_authenticated:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                recipient_account.balance += amount
                self.transaction_history.append(f"Transferred ${amount:.2f} to recipient account")
                print(f"Transferred ${amount:.2f} to recipient account.")
            else:
                print("Invalid transfer amount.")
        else:
            print("Please authenticate first.")

    def display_transaction_history(self):
        if self.user_authenticated:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("Please authenticate first.")

    def quit(self):
        print("Thank you for using our ATM. Goodbye!")

if __name__ == "__main__":
    user_account = ATM(1000)

    while True:
        print("\nATM Menu:")
        print("1. Authenticate")
        print("2. Display Balance")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            user_account.authenticate(user_id, pin)
        elif choice == "2":
            user_account.display_balance()
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            user_account.withdraw(amount)
        elif choice == "4":
            amount = float(input("Enter the deposit amount: "))
            user_account.deposit(amount)
        elif choice == "5":
            recipient_account = ATM(0)
            amount = float(input("Enter the transfer amount: "))
            user_account.transfer(recipient_account, amount)
        elif choice == "6":
            user_account.display_transaction_history()
        elif choice == "7":
            user_account.quit()
            break
        else:
            print("Invalid choice. Please select a valid option.")


