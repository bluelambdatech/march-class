def calculus():
    return 200 * 40

def diff():
    return "Okafor"

def inte():
    return "Nathan"

def multiply(x,y):
    return x*y

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y


# Classes
class Calculus:
    name = "Nathan"

    def __init__(self, lname, fname):
        self.lastname = lname
        self.firstname = fname
        self.fullname = f'{lname} {fname}'
    def multiply(self,x, y):
        num1 = x * y
        num2 = x + y

        return num1 / num2

    def addition(self,x, y):
        self.number = 300
        print(self,fullname)
        return x + y

    def subtraction(self,x, y):
        print(self.fullname)
        print(self.multiply(x,y))
        self.addition(x,y)
        print(self,number)
        return x - y

CalCare = Calculus("Adaramola", "Bukola")

CalCare.subtraction(20,20)