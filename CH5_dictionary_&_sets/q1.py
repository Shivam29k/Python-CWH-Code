# Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up! 

Dict = {
    'admi':'men',
    'aurat':'women ',
    'insaan':'human',
    'beti':'daughter',
    'beta':'son',
    'tanki':'tank',
    'sadak':'road'
}

hindi = input('hindi word: ')

# print("english meaning: ", Dict[hindi])

#below line will not get an error if the word isnt present in dict
# print("english meaning: ", Dict.get(hindi))



# when wrong word is given writ a code to output "not in Dict"
a = str(Dict.get(hindi))
if a == "None":
    print("word isn't in Dict")
else:
    print("English meaning:",Dict[hindi])
