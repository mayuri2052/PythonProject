class Date:
    __dd = None
    __mm = None
    __yy = None

    def __init__(self, dd, mm, yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def showDate(self):
        print("The date is "+str(self.__dd)+"/"+str(self.__mm)+"/"+str(self.__yy))


