# FINDING FACTORIAL

def factorial(num):
    if num == 1 or num == 0:   #Base condition which dosent calls the factorial any further
        return 1
    else:
        return num*factorial(num-1) #Function calling itself

num = int(input())

print(factorial(num))

# This is how this will work 
# factorial(4)
# 4*factorial(3)
# 4*3*factorial(2)
# 4*3*2*factorial(1)
# 4*3*2*1