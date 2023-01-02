# A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

a = input()
spam = ["make a lot of money", "buy now", "subscribe this", "click this"]

if a in spam:
    print("spam hai saale ko block karo ")
else:
    print("spam nai hai ")
