class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.__balance}")

    def withdraw(self, amount):
        # FIX: Removed the '-' sign. Also added '=' to allow withdrawing full balance.
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}. Remaining amount: ${self.__balance}")
        else: 
            print("Insufficient Balance")

    def display(self):
        print(f"Account Holder: {self.name} | Balance: ${self.__balance}")
        
class Savings(Bank): # Inheritance
    def __init__(self, name, balance, interest=0.04):
        super().__init__(name, balance)
        self.interest = interest

    def display(self): # Method overriding
        # Note: Child class can't access __balance directly, so we use parent's logic or a getter
        print(f"[Savings] Holder: {self.name} | Interest Rate: {self.interest*100}%")

# Real world operations
print("********* Welcome to XYZ Bank System ************")
acc1 = Bank("Raghu", 50000)
acc2 = Savings("Vamshi", 80000)

acc1.withdraw(1000)
acc1.display()
print("-" * 30)

acc2.deposit(10000)
acc2.display()