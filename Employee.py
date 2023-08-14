from Person import Person

class Employee(Person):
    __empID = None
    __baseSal = None

    def __init__(self, empId, baseSal, name, dd, mm, yy):
        self.__empID = empId
        self.__baseSal = baseSal
        Person.__init__(self, name, dd, mm, yy)

    def showEmployee(self):
        print("Basic salary of empid "+str(self.__empID)+" is` "+str(self.__baseSal))
        self.showPerson()

    def calsal(self):
        return self.__baseSal

