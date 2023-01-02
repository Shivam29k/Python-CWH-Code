# Write a class calculator capable of finding square, cube, and the square root of a number.

class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f'Square of {self.n} is {self.n**2}')

    def sqrt(self):
        print(f'Suare root of {self.n} is {self.n**(1/2)}')

    def cube(self):
        print(f'Cube of {self.n} is {self.n**3}')

    @staticmethod
    def gide():
        print('First Enter the number.\nThen enter the operation you want (square, sqrt or cube ?)')


Calculator.gide()

n = int(input())
calculate = Calculator(n)


what = input()
if what == "square":
    calculate.square()
elif what == "sqrt":
    calculate.sqrt()
elif what == "cube":
    calculate.cube()
