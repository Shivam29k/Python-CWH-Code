# write a list comprehension to print a list which contains the multiplication tabl of a user enterd number

n = int(input("Enter your number: "))

table = [n*i for i in range(1,11)]
print(table)