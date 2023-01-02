S = set()
S.add(1)
S.add(2)
print(S)
#or
Set = {1,2}
Set.add(3)
# Set.add([6,7,8]) not possible coz list can be changed 
# Set.add({a:b}) dect bhi cant be added coz wo bhi change ho sakte hai
Set.add((6,7,8)) #possible coz tuple cant be changed 
print(Set)
