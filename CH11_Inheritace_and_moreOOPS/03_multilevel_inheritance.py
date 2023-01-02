class Person:
    country = 'India'

    def takeBreath(self):
        print('I m breathing.....')

class Employee(Person):
    company = "honda"

    def getSalary(self):
        print(f'Salary is {self.salary}')
    
    def takeBreath(self):
        print('I m an employee so i m luckily breathing..')

class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print("No salary to programmers")

p = Person()
p.takeBreath()
e = Employee()
e.salary = 10000
e.takeBreath()
e.getSalary()
pr = Programmer()
pr.takeBreath()
pr.getSalary()

print(pr.country)