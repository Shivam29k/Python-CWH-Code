class Employee:  # Base class
    company = 'Google'

    def showDetails(self):
        print('This is an employee')


class Programmer(Employee):  # Derived or Child Class
    language = 'Python'

    def getlanguage(self):
        print(f'The language is {self.language}')

    def showDetails(self):
        print('This is an programmer')


e = Employee()
e.showDetails()
# Employee.showDetails(e)

p = Programmer()
p.getlanguage()
p.showDetails()
print(p.company)
