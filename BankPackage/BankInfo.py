class Account:
    def __init__(self,in_balance,name):
        self.name=name
        self.balance= in_balance
        print("constructer called")


    def Deposit(self,deposit):
        self.balance = self.balance + deposit
        return self.balance

    def Withdrawal(self,withdraw):
        self.balance =self.balance - withdraw
        return self.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self,other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self,other):
        return self.balance <= other.balance
