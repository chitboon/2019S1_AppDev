class BankAccount:

    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('You have insufficient amount to withdraw!')

    def deposit(self, amount):
        if amount >0:
            self.__balance += amount


    def get_interest_rate(self):
        if self.__account_number.startswith('1'):
            return 0.01
        elif self.__account_number.startswith('0'):
            return 0.005
        else:
            print('Invalid account number')
            return 0

    def get_interest(self):
        return self.__balance * self.get_interest_rate()


account = BankAccount('00-12345-11')
account.deposit(500)
print('Your account number is', account.get_account_number())
print('You have', account.get_balance())
account.withdraw(100)
print('You are left with', account.get_balance())
print('Your interest rate is', account.get_interest_rate())
print('Your interest earned is', account.get_interest())
