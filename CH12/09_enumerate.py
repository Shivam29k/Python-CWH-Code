list1 = [2, 34, 45, 6.2, "Shivam", False]

# one way
index = 0
for item in list1:
    print(index, item)
    index +=1

print("--------------------")

# other way by using enumerate function
# enumerate function initates a counter, which starts from 0
for i, items in enumerate(list1):
    print(i, items)