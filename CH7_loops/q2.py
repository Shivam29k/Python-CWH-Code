# Write a program to print the multiplication table of a given number using for loop.

a = int(input("number: "))

i = 1
while i < 11:
    print(a,"*",i,"=",a*i)
    i = i+1
