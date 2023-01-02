# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please”.
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

import random

num = random.randint(1,100)
print(num)

def afterGame(guessCount):
    with open("highSCore.txt", "r") as f:
        hiScore = int(f.read())

    # print(hiScore)
    # print(guessCount)
    if (hiScore >= guessCount):
        print("Yoooo!!!!! You Guessed the number in lowest no. of guesses till now.\nCONGO CONGO")
        with open("highSCore.txt", "w") as f:
            f.write(str(guessCount))


def game(inputNum, guessCount, randomNum=num):
    # No. of counts
    guessCount += 1

    # input number is smaller
    if inputNum < randomNum:
        print("Higher Number Please")
        inputNum = int(input("try yuour guess again : "))
        game(inputNum, guessCount)

    # input number is greater
    elif inputNum > randomNum:
        print("lower Number Please")
        inputNum = int(input("try yuour guess again : "))
        game(inputNum, guessCount)


    # number guessed correctly
    elif inputNum == randomNum:
        print(f"Ayoo it took you took {guessCount} chances to guess it Correctly")
        
        return afterGame(guessCount)


print("Computer has randomly choosen a word to guess between 1 to 100.\nTry guessing it.")

inputNum = int(input("Start your Guess game from here..... : "))

game(inputNum, 0)


