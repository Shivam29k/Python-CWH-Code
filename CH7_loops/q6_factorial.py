# factorial

n = int(input("Enter number\n"))

factorial = 1
i = 0
for  i in range (0,n):
    i+=1
    factorial = factorial*i
print(f"The factorial of {n} is {factorial}")