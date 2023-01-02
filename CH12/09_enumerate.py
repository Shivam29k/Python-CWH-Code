list1 = [2, 34, 45, 6.2, "Shivam", False]

# one way
index = 0
for item in list1:
    print(index, item)
    index +=1

print("--------------------")

# other way
for i, items in enumerate(list1):
    print(i, items)