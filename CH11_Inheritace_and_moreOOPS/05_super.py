class Person:
    country = 'India'

    def __init__(self):
        print("initializig person....")

    def takeBreath(self):
        print('I m breathing.....')

class Employee(Person):
    company = "honda"

    def __init__(self):
        super().__init__()
        print('initializing employee....')

    def getSalary(self):
        print(f'Salary is {self.salary}')
    
    def takeBreath(self):
        super().takeBreath()
        print('I m an employee so i m luckily breathing..')

class Programmer(Employee):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("initializing programmer...")
    
    def getSalary(self):
        print("No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()
        print("I m breathing++..")

p = Person()
e = Employee()
e.salary = 10000
pr = Programmer()
pr.takeBreath()
