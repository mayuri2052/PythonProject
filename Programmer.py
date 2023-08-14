from Employee import Employee

class Programmer(Employee):
    __projectName = None
    __km = None
    __cpk = None

    def __init__(self, projectname, km, cpk, empid, basesal, name, dd, mm, yy):
        self.__projectName = projectname
        self.__km = km
        self.__cpk = cpk
        Employee.__init__(self, empid, basesal, name, dd, mm, yy)

    def showProgrammer(self):
        print("Programmer has project statement as "+str(self.__projectName))
        self.showEmployee()

    def calsal(self):
        netsal = Employee.calsal(self) +(self.__km * self.__cpk)
        return netsal