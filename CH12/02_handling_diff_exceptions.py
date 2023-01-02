try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("exception 1 occured : PLease Enter a valid value")
    print(e)
except ZeroDivisionError as e:
    print("exception 2 occured : make sure you are not dividing by zero")
    print(e)
except:
    print("its an error")

print("Thanks for using the code!!")