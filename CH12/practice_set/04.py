# write a program to display a/b where a and b are intgers. If b = 0, deisply by errorhandling the zerodivisionerror
a = int(input("enter a: "))
b = int(input("enter b: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("Infinite")