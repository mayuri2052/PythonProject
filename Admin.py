from Employee import Employee


class Admin(Employee):
    __BUName = None
    __km = None
    __cpk = None

    def __init__(self, buname, km, cpk, empid, basesal, name, dd, mm, yy):
        self.__BUName = buname
        self.__km = km
        self.__cpk = cpk
        Employee.__init__(self, empid, basesal, name, dd, mm, yy)

    def showAdmin(self):
        print("Admin has BU Name as " + str(self.__BUName))
        self.showEmployee()

    def calsal(self):
        netsal = Employee.calsal(self) + (self.__km * self.__cpk)
        return netsal