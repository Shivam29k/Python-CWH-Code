# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.
def game(n):
    return int(n)


def highScore(n):
    f = open("highScore.txt")
    hS = int(f.read())
    print(f"previous High Score is {hS}")
    if hS < score:
        f = open('highScore.txt', 'w')
        f.write(str(score))
        f.close()
        f = open('highScore.txt')
        hS = int(f.read())
        print(f"{hS} is new high Score")
    else:
        print(f"your score is {hS}")


n = input()
score = game(n)
highScore(n)


def game():
    return 64


score = game()
with open('highscore.txt') as f:
    hiscore = int(f.read())
if hiscore < score:
    with open('highScore.txt', 'w') as f:
        f.write(str(score))
