from Employee import Employee

class SalesManager(Employee):
    __target = None
    __comm = None
    __km = None
    __cpk = None

    def __init__(self, target, km, cpk, empid, basesal, name, dd, mm, yy):
        self.__target = target
        self.__km = km
        self.__cpk = cpk
        Employee.__init__(self, empid, basesal, name, dd, mm, yy)

    def showSalesManager(self):
        print("Salesmanager have "+str(self.__target)+" with the "+str(self.__km)+" charge per kilometer "+str(self.__cpk))
        self.showEmployee()

    def calsal(self):
        netsal = Employee.calsal(self) + (self.__target * 0.1) + (self.__km * self.__cpk)
        return netsal

