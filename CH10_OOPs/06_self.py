class Employee:
    company = 'Google'

    def getSalary(self):
        print("Salary is 100k US$")

    def getRole(self, a):
        print(
            f"for the employee ie {self.name} working in {self.company} is a {self.role}\n"+a)


harry = Employee()
harry.name = 'harry'
harry.role = "Senior Developer"

harry.getSalary()
# ---> This turn automatically to

# Employee.getSalary(harry)

# this means it will pass an argument 'harry' in getSalary('harry')
# SO we use Self to make positional argument

harry.getRole('Thanks!')
