class Number:
    def sum(self):
        return self.a + self.b

    def product(self):
        return self.a*self.b


num = Number()
num.a = 4
num.b = 5
s = num.sum()
print(s)
print(num.product())
