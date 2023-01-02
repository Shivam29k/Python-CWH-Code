class Remote:
    def leftKey(self):
        pass

    def rightKey(self):
        pass

    def downKey(self):
        pass

    def upKey(self):
        pass


class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveDown(self):
        pass

    def moveUp(self):
        pass


remote1 = Remote()
player1 = Player()

if (remote1.leftKey()):
    player1.moveLeft()
elif (remote1.rightKey()):
    player1.moveRight()
elif (remote1.downKey()):
    player1.moveDown()
elif (remote1.upKey()):
    player1.moveUp()
