from MBBank import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount


B1 = BankAccount(1112,500)
B1.displaybalance()
B1.withdraw(200)
B1.deposit(700)
B1.displaybalance()

print("==================================================")

s1 = SavingAccount(1111,1000)
s1.displaybalance()
s1.savdeposit(2000)
s1.displaybalance()
s1.withdraw(4000)

print("===================================================")

c1 = CurrentAccount(1113,100000)
c1.displaybalance()
c1.curwithdrwal(99800)
c1.displaybalance()

print("====================================================")

B2 = BankAccount(1114,3000)
B2.displaybalance()
B2.transfer(500, B1)
B1.displaybalance()
B2.displaybalance()

