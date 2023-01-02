t = (1, 42, 3, 4, 5, 6, 7, 8, 9, 23, 565)

print(t.count(3)) #It will return the number of times 1 occurs in a.
print(t.index(42)) #output will be index no of 42
print(len(t))  #To determine how many items a tuple has

if 1 in t:
    print("yes one is in this tuple")

print(type(t))

l = list(t)  # convert tupe into list 
print(type(l)) 

#so to add item or to do anything in tuple forst convert it to list then do it then convert back to tuple
thistuple = ("qwertyuiop", "asdfghjkl","zxcvbnm")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#to remove something from tuple
y = list(thistuple)
y.remove("qwertyuiop")
thistuple = tuple(y)
print(thistuple)

del thistuple #this will delete the tuple 
# print(thistuple) # this will raise an error coz the tuple is deleted 

# addation of two tuple 
thistuple = ("qwertyuiop", "asdfghjkl","zxcvbnm")
y = ("orange",)
thistuple += y
print(thistuple)
