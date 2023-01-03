n = int(input("Enter your number: "))

table = [n*i for i in range(1,11)]

with open("tables.txt","w") as f:
    f.write(str(table))