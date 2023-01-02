while(True):
    try:
        i = int(input("Enter a number: "))
        c = 1/i
    except Exception as e:
        print(e)
# will go for else if except execute nai hua
    else:
        print("We were successful")
    