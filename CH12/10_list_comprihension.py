a = [3, 4, 5, 7, 6, 8, 45, 565, 67, 34, 67]

# one way 
b = []
for item in a :
    if item%2 == 0:
        b.append(item)
print(b)


# other way
c = [i for i in a if i%2==0]
print(c)

t = [1, 4, 4, 2, 6, 12, 1]
s = {i for i in t}
print(s)