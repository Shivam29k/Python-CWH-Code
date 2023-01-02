# Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.
f = open("poems.txt", "r")
t = f.read()
if "twinkle" in t:
    print("poem contains twinkle")
else:
    print("poem dosent contains the word twinkle")

f.close()
