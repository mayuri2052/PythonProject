print("Welcome to MB bank ")


class BankAccount:
    _currentBalance = None
    _accNo = None
    def __init__(self, no, initialAmount):
        self._currentBalance = initialAmount
        self._accNo = no
        # print("Congratulations... Your Account has been created")

    def displaybalance(self):
        print(str(self._accNo) + " Your current balance is "+str(self._currentBalance))

    def deposit(self, amount):
        self._currentBalance += amount
        print(str(amount) + " is deposited in your account " + str(self._accNo))

    def checkbalance(self, amount):
         if self._currentBalance < amount:
             return False
         else:
             return True

    def withdraw(self, amount):
        if self.checkbalance(amount):
            self._currentBalance -= amount
            print(str(amount) + " is withdrawl from your account " + str(self._accNo))
        else:
            print("Insufficient amount in account " + str(self._accNo))

    def transfer(self, amount, bankAccount):
        self.withdraw(amount)
        bankAccount.deposit(amount)




