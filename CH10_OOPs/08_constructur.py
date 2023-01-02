class Employee:
    company = 'Google'

    # __init__ is called constructor essko call nai kart ye apne aap call ho jata hai if u put any object in a class
    def __init__(self, name, salary, role):
        print("Employee is Created!")
        self.name = name
        self.salary = salary
        self.role = role

    def getSalary(self):
        print("Salary is 100k US$")

    def getInfo(self, a):
        print(
            f'{self.name} is {self.role} of the {self.company} and his salary is {self.salary} \n{a}')


# just setting the object will run constructur
shivam = Employee('Shivam', 100, 'CEO')

shivam.getInfo('Thanks!')
