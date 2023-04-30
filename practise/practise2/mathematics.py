
def calculus():
    return 230 * 40


def diff():
    return "Omolewa"


def inte():
    return "Daniel"


def multiply(x, y):
    return x * y


def addition(x, y):
    return x + y


def substraction(x, y):
    return x - y


# Classes
class Mathematics:
    name = "Omolewa"

    def __init__(self, lname, fname):
        self.lastname = lname
        self.firstname = fname
        self.fullname = f'{lname} {fname}'

    def multiply(self, x, y):
        num1 = x * y
        num2 = x + y

        return num1 / num2

    def addition(self, x, y):
        self.number = 400
        print(self.fullname)
        return x + y

    def substraction(self, x, y):
        print(self.fullname)
        print(self.multiply(x, y))
        self.addition(x, y)
        print(self.number)
        return x - y


mathmath = Mathematics("Adaramola", "Bukola")

mathmath.substraction(20, 20)



