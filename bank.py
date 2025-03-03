class Account:
    def __init__(self, acct_type, min_balance=500):
        self.acct_type = acct_type
        self.min_balance = min_balance
        self.current_balance = 0
    
    def withdraw(self, amount):
        if self.current_balance - amount < 0:
            print("Insufficient funds!")
        else:
            self.current_balance -= amount
            print("You withdrew: ",amount,"New balance:  ",self.current_balance)

    def deposit(self, amount):
        self.current_balance += amount
        print("You deposited",amount,"New balance:  ",self.current_balance)


class Checking(Account):
    def __init__(self, acct_type, min_balance=500):
        super().__init__(acct_type, min_balance)
        self.over_draft = 1000
    
    def withdraw(self, amount):
        if self.current_balance - amount < -self.over_draft:
            print("Overdraft limit exceeded!")
        else:
            self.current_balance -= amount
            if self.current_balance < 0:
                self.over_draft += 200
                print("Warning: Overdraft increased by 200. New overdraft limit: ",self.over_draft)
            print("You Withdrew",amount, "New balance: ",self.current_balance)


class Savings(Account):
    def __init__(self, acct_type, min_balance=500):
        super().__init__(acct_type, min_balance)
        self.over_draft = 1200
        self.deposit_count = 0
    
    def withdraw(self, amount):
        if self.current_balance - amount < -self.over_draft:
            print("Overdraft limit exceeded!")
        else:
            self.current_balance -= amount
            if self.current_balance < 0:
                self.over_draft += 200
                print("Warning: Overdraft increased by 200. New overdraft limit: ",self.over_draft)
            print("Withdrew",amount,"New balance: ",self.current_balance)

    def profit(self):
        profit_amount = self.current_balance * 0.15
        self.current_balance += profit_amount
        print("Profit added: ",profit_amount, "New balance:  ",self.current_balance)

    def deposit(self, amount):
        super().deposit(amount)
        self.deposit_count += 1
        if self.deposit_count % 10 == 0:
            self.profit()


class Person:
    def __init__(self, name, acct_type):
        self.name = name
        if acct_type == "Checking":
            self.account = Checking(acct_type)
        elif acct_type == "Savings":
            self.account = Savings(acct_type)
        else:
            raise ValueError("Invalid account type. Choose 'Checking' or 'Savings'")
    
    def deposit(self, amount):
        self.account.deposit(amount)
    
    def withdraw(self, amount):
        self.account.withdraw(amount)


# Example usage
person1 = Person("Shawn", "Checking")
person1.deposit(1000)
person1.withdraw(1500)
person1.deposit(1500)

person2 = Person("Jane", "Savings")
person2.deposit(1000)
person2.deposit(200)
person2.withdraw(100)
person2.deposit(300)
person2.deposit(400)
person2.deposit(500)
person2.deposit(600)
person2.deposit(700)
person2.deposit(800)  # This triggers profit() for the 10th deposit
