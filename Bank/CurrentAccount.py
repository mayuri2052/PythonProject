from MBBank import BankAccount
class CurrentAccount(BankAccount):


    def __init__(self, no, initialAmount):
        super().__init__(no, initialAmount)
        print("Congratulations... Your Current Account has been created" + str(self._accNo))

    def curwithdrwal(self, amount):
        amount += 200
        print("Charge 200 is applicable for every withdraw")
        self.withdraw(amount)
