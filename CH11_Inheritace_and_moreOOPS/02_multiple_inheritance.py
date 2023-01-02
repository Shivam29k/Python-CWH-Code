class Employee:
    company = "Visa"
    eCode = 120


class Freelancer:
    company = "Fiver"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer (Employee, Freelancer):
    name = "Rohit"


p = Programmer()
p.upgradeLevel()
print(p.level)
# Employee parent class is preffered coz we have mentiond it before freelancer iinside progrmmer class
print(p.company)
