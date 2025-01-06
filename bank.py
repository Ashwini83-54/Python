class bankAccount:
    def __init__(self, amount, name):
        if amount <= 0:
            self.bal = 0
        else:
            self.bal = amount
        self.name = name
        
    def withdraw(self, amount):
        self.bal -= amount
        
    def deposit(self,amount):
        self.bal += amount
        
    def display(self):
        print("Your balance is", self.bal)
        
b1 = bankAccount(100, "xyz")
b1.display()
b1.withdraw(50)
b1.display()
b1.deposit(300)
b1.display()
        
