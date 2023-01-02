
# Write a python program using the function to convert Celsius to Fahrenheit.

def ctof (c):
    return (c * 9/5) + 32 

print(ctof(50))


# How do you prevent a python print() function to print a new line at the end?()
print("hELLO", end=" " )
print("how", end=" " )
print("are", end=" " )
print("you", end="\n" )

print("hELLO", end="" )
print("how", end="" )
print("are", end="" )
print("you", end="" )

# Default is \n
print("hELLO", end="\n" )
print("how", end="\n" )
print("are", end="\n" )
print("you", end="\n" )


# Write a python function to print the first n lines of the following pattern.

n=3
for i in range (n):
    print("*"*(n-i))


# Write a python function to remove a given word from a list and strip it at the same time.

def remove_word_strip( string , word):
    newStr = string.replace(word,"")
    newStr = newStr.strip()
    return print(newStr)

this = "      Shivam IS Best    "
remove_word_strip(this , "Shivam")


# Write a python function to print the multiplication table of a given number.

# def multiplicationTable(n):
#     return for i in range(10):
#              print(f"{n} x {i+1} = {n*(i+1)}")
    
# multiplicationTable(3)


