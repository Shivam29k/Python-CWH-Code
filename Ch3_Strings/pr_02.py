# Write a program to fill in a letter template given below with name and date.
# letter = ‘’’ Dear <|NAME|>,

#                         You are selected!

#                         <|DATE|>
Letter = '''Dear <|NAME|>
Greetings from ABC coding house
You are selected!
Date : <|DATE|>'''

name = input("Enter ur name \n")
date = input("Enter dtae \n")

Letter = Letter.replace("<|NAME|>",name)
Letter = Letter.replace("<|DATE|>",date)
print(Letter)
