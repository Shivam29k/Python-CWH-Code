while(True):
    try:
        i = int(input("Enter a number: "))
        c = 1/i
    except :
        exit()
# Unlike else finally will always be executed
# even if the program is exited at except, finally will be executed.(but print statement wont be)
    finally:
        print("We were done")
    print("thanks for using the program")