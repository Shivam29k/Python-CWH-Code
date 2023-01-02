# Write a program to greet all the person names stored in a list l1 and which starts with S.

l1 = ["Shivam","Shubham","sahil","yash","hunny","Nishant","Ankit","Divyanshu","Sanjana","Sameer","Suprabha"]

l = len(l1)
# print(l)

# for i in range (l):
#     if l1[i][0] == "S" or l1[i][0] == "s":
#         print ("howdy",l1[i])
#     else:
#         pass



#Using while loop
i = 0
while i <= l:
    if l1[i][0] == "S" or l1[i][0] == "s":
        print("Howdy",l1[i])
        i  = 1+i
    else:  
        i = 1+ i
    
         