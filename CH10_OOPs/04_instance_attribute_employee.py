class Employee:
    company = 'Google'  # Class Attribute
    salary = 100  # Class Attribute


harry = Employee()
shivam = Employee()

print(harry.company)
Employee.company = 'meta'     # Class Attribute
print(shivam.company)

# Instance attribute >>>>> Class Attribute

shivam.salary = 300   # Instance attribute

print(harry.salary)
print(shivam.salary)
