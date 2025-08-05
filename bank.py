class customer:
    def __init__(self,name,address,contact):
        self.name=name
        self.address=address
        self.contact=contact
class account:
    def __init__(self,acc_number,customer):
        self.acc_number=acc_number
        self.customer=customer
        self.balance=0
        self.transactions=[]
    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(f"Deposited{amount}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.transactions.append(f"Withdrew:{amount}")
        else:
            print("Insufficient")
    def show_balance(self):
        print(f"Balance:{self.balance}")