# Write a program using the function to find the greatest of three numbers.

def maximum (num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
         if num2>num1:
            if num2>num3:
                return num2
            else:
                return num3

n1 = int(input("num1: "))
n2 = int(input("num2: "))
n3 = int(input("num3: "))

max = maximum(n1,n2,n3)

print(f"The maximum value is {max}")




