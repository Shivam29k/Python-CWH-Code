a = 54  # Global variable 
b = 64

def func1():

    a = 8  # Local variable
    print("a:", a)

    global b  # way to create global variable
    b = 18
    print("b:",b)

    c  = 69

func1()
print("a:",a)
print("b:",b)
# below will be an error
# print("c:",c)