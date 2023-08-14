
from Date import Date
from Person import Person
from Employee import Employee
from SalesManager import SalesManager
from Programmer import Programmer
from Admin import Admin

D1 = Date(1, 2, 31)
D1.showDate()

p1 = Person("Rishi", 1,2,31)
p1.showPerson()
print("_____________________________")
e1 = Employee(200, 30000, "Mayuri", 3,1,23)
e1.showEmployee()

print("_____________________________")
s1 = SalesManager(2000 ,100, 9, 17, 3000, "Avik", 2, 5, 20)
s1.showSalesManager()
print("Cal " + str(s1.calsal()))

print("_____________________________")
s1 = Programmer("SMOP" ,100, 9, 17, 3000, "Avik", 2, 5, 20)
s1.showProgrammer()
print("Cal " + str(s1.calsal()))

print("_____________________________")
s1 = Admin("SMOP" ,100, 9, 17, 3000, "Avik", 2, 5, 20)
s1.showAdmin()
print("Cal " + str(s1.calsal()))
