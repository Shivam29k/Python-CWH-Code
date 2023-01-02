x = int(input("Enter num: "))

primeList = []
cumpositeList = []
notAny = [1]
for j in range (2,x):
    prime  = True
    
    for i in range (2,j):
        if j%i == 0:
            prime  = False
            break
            
    if prime:
        primeList.append(j)
    else:
        cumpositeList.append(j)


print("prime numbers", primeList)
print("Cumposite numbers", cumpositeList)
print("Neither prime nor cum", notAny)