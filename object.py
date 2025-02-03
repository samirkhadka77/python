class account():
    def __init__(self, name, bal, acc):
        self.name = name
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "is debited from", self.account_no)
        print("total balance", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "is credited to", self.account_no)
        print("total balance", self.balance)

    def get_balance(self):
        return self.balance


acc1 = account("samir", 20000, 173219012)

print(acc1.name,acc1.balance,acc1.account_no)

acc1.debit(5000)
acc1.credit(8000)