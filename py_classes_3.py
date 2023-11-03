class Account:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def print_balance(self):
        print(f"Balance for Account {self.acc_no} is ksh {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc1 = Account("June", "0001", 75000)  # Creating an instance of the Account class
acc2 = Account("Alice", "002", 23490)

acc1.print_balance()  # Printing the initial balance
acc1.deposit(5000)  # Depositing 500 KSH
acc1.print_balance()  # Printing the new balance after the deposit
acc1.withdraw(12000)  # Withdrawing 200 KSH
acc1.print_balance()  # Printing the balance after the withdrawal
