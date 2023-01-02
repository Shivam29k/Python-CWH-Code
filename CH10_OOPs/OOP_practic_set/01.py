# Create a class programmer for storing information of a few programmers working at Microsoft.
class Programmer:
    company = 'Microsoft'

    def __init__(self, name, role, salary):
        self.name = name
        self.salary = salary
        self.role = role

    def getInfo(self):
        print(f'{self.name} works in {self.company}')
        print(f'{self.name} is on {self.role} position')
        print(f'{self.name} earns {self.salary}. \n')


programmer1 = Programmer('Shivam', 'CEO', 100000)
programmer2 = Programmer('Sahil', 'slave', 10000)
programmer3 = Programmer('Hunny', 'waiter', 1000)

programmer1.getInfo()
programmer2.getInfo()
programmer3.getInfo()
