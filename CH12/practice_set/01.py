# write a program to open three files 1.txt, 2.txt, 3.txt, If any of these files are not present , message without exiting the program must be printed prompting the same.

def openFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} not found")

openFile("1.txt")
openFile("2.txt")
openFile("3.txt")