x =  int(input("Enter number\n"))

prime = True

for i in range (2,x):
    if (x%i == 0):
        prime = False
        break

if prime:
    print(f"{x} prime")
else:
    print(f"{x} not prime")
