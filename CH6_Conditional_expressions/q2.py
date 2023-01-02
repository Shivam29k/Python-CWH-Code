# Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
t = int(input("Max marks each sub\n"))
p = int(input("Physics marks\n "))
c = int(input("Chem marks\n "))
m = int(input("Maths marks\n "))

a =  (p/t)*100 
b =  (c/t)*100 
c =  (m/t)*100 

d = ((p+c+m)/(3*t))*100

if a>33 and b>33 and c>33 and d>44:
    print("ladka paas ho gaya")
else:
    print("Bt ho gai")
