#!/usr/bin/python3
"""
Checkbook Program

This program simulates a simple checkbook where a user can deposit,
withdraw, and check their balance. It includes error handling to
prevent crashes due to invalid input.
"""

class Checkbook:
    """A simple Checkbook class to manage deposits and withdrawals."""

    def __init__(self):
        """Initialize a new Checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit the given amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit. Must be a positive number.

        Returns:
            None
        """
        if amount <= 0:
            print("Please enter a positive amount.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw the given amount from the checkbook.

        Parameters:
            amount (float): The amount to withdraw. Must be less than or equal to the balance.

        Returns:
            None
        """
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """Main loop that runs the checkbook program."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            print("Thank you for using the Checkbook program!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

