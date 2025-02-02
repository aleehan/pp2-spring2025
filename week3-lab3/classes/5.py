class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        self.balance += int(input(f"How much do you want to add, {self.owner}?: "))

    def withdraw(self):
        self.sum_of_withdraw = int(input("How much do you want to withdraw?: "))
        if self.sum_of_withdraw > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= self.sum_of_withdraw

    def interface(self):
        print(f"Hello {self.owner}!")
        while True:
            print(f" 1 - My account\n 2 - My balance\n 3 - Add money\n 4 - Withraw money\n 5 - Exit")
            self.choose = int(input("Your choose: "))
            if self.choose == 1: 
                print(f"Your account is - {self.owner}!")
            elif self.choose == 2:
                print(f"Your balance: {self.balance}$")
            elif self.choose == 3:
                self.deposit()
            elif self.choose == 4:
                self.withdraw()
            elif self.choose == 5:
                return False
            
name = input("Wtite your name: ")
owner = Account(name)
owner.interface()

