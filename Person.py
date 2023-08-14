from Date import Date
class Person:
    __name = None
    __DOB = None

    def __init__(self, name, dd, mm, yy):
        self.__name = name
        self.__DOB = Date(dd,mm,yy)



    def showPerson(self):
        print("Person name is "+str(self.__name))
        print("Person date of birth is")
        self.__DOB.showDate()

