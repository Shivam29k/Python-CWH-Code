# Write a program to sum a list with 4 numbers. 
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

nums = [n1, n2, n3, n4]
sum1 = nums[0] + nums[1] + nums[2] + nums[3]
print(sum1)

#another method
print(sum(nums))