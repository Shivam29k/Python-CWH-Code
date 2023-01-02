# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100	Ex
# 80-90	    A
# 70-80	    B
# 60-70	    C
# 50-60	    D
# <50	    F

x = int(input())

if 90<x and x<=100:
    print("EX")
elif 80<x and x<=90:
    print("A")
elif 70<x and x<=80:
    print("B")
elif 60<x and x<=70:
    print("C")
elif 50<x and x<=60:
    print("D")
else:
    print("F")