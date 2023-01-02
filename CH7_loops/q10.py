# Write a program to print the multiplication table of n using for loop in reversed order.
num = int(input("Enter number:\n"))

a = 10  
for i in range(1,11):
    print(f"{num} x {a} = {num*a}")
    a = a-1
