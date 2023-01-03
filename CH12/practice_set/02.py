# write a program to print third, fifth ans seventh element from a list using enumerate function.
l1 = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, items in enumerate(l1):
    if i == 3 or i == 5 or i == 7:
        print(items)
