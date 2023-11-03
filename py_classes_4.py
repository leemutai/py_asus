class Account:
    def __init__(self, name, number, balance):
        self.acc_name = name
        self.acc_number = number
        self.acc_balance = balance

    def deposit(self, amount):
        self.acc_balance += amount

    def withdraw(self, amount):
        if amount > self.acc_balance:
            print(f"Insufficient funds. Balance is {self.acc_balance}")
        else:
            self.acc_balance -= amount

    def __str__(self):
        return f"name:{self.acc_name}, accNo: {self.acc_number}, balance{self.acc_balance}"


class DollarAccount(Account):
    def rates(self):
        return 153.89

    def deposit(self, amount):
        usd = amount / self.rates()
        self.acc_balance += usd


dc1 = DollarAccount("Jerry", "d-0001", 3200)
dc1.withdraw(500)
print(dc1.acc_balance)
print(dc1.rates())
dc1.deposit(20000)
print(dc1.acc_balance)

# # define a parameter that will return the acc balance with 2 dp
# acc1 = Account("Jude", "0001", 11000)
# acc1.deposit(500)
# print(acc1)
#
# # #named parameters
# acc2 = Account(balance=14000, name="Henrik", number="0002")
# acc2.deposit(600)
# print(acc2)
