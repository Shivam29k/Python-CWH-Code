# Write a program to find the greatest of four numbers entered by the user.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a>b and a>c and a>d):
    print(a)

if (b>a and b>c and b>d):
    print(b)

if (c>b and c>a and c>d):
    print(c)

else:
    print(d)

