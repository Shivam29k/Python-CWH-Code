s = {1,2,3,4}

s.remove(2) #removes 2 from the set
print(s)

s = {1,2,3,4}

print(len(s)) #counts the length of set
print(s.pop()) #pops an arbitrary value

s.clear() #clears the set
print(s)

s = {1,2,3,4}
print(s.union({5,6,7})) #maths wala union
print(s.intersection({1,3,9,0})) #maths wala intersection
