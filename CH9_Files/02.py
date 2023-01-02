f = open("E:\Codes\python\CWH\CH9_Files\sample.txt", "a")
f.write("This is new content.")
f.close()

f = open("demo2file.txt", "w")
f.write("This is the content")
f.close()

f = open("demo2file.txt", "rt")
print(f.read())
f.close()

f = open("demo2file.txt", "a")
f.write(" I m appending")
f.close()

f = open("demo2file.txt", "r")
print(f.read())
f.close()

f = open("demo2file.txt", "rb")
print(f.read())
f.close()
