a = input("")
b = a[1]

if(b >= "a" and b <= "z" or b >= "A" and b <= "Z"):
    print("It's an alphabet")
elif( b >= "0" and b <= "9"):
    print("It's a digit")
else:
    print("It's a charcter")
