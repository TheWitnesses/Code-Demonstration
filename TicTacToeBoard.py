class Board:
    def __init__(self):# Create board table
        self._unusedBoxes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #Keeps track of status of the game
        self._mainBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._gameOver = False
        self._winner = False
        self._keyOffset = 48

    def checkWin(self, val, displaycallback):  # checks for winner of game
        print (self._mainBoard)

        gameEnded = False
        if self._mainBoard[0] == val and self._mainBoard[1] == val and self._mainBoard[2] == val:
            displaycallback(val)
            gameEnded = True

        elif self._mainBoard[3] == val and self._mainBoard[4] == val and self._mainBoard[5] == val:
            displaycallback(val)
            gameEnded = True

        elif self._mainBoard[6] == val and self._mainBoard[7] == val and self._mainBoard[8] == val:
            displaycallback(val)
            gameEnded = True

        elif self._mainBoard[0] == val and self._mainBoard[3] == val and self._mainBoard[6] == val:
            displaycallback(val)
            gameEnded = True

        elif self._mainBoard[1] == val and self._mainBoard[4] == val and self._mainBoard[7] == val:
            displaycallback(val)
            gameEnded = True

        elif self._mainBoard[2] == val and self._mainBoard[5] == val and self._mainBoard[8] == val:
            displaycallback(val)
            gameEnded = True

        elif self._mainBoard[2] == val and self._mainBoard[4] == val and self._mainBoard[6] == val:
            displaycallback(val)
            gameEnded = True

        elif self._mainBoard[0] == val and self._mainBoard[4] == val and self._mainBoard[8] == val:
            displaycallback(val)
            gameEnded = True

        else:
            return gameEnded

        return gameEnded

    def removeChoice(self, val): # Removes variable choice
        for i in range(0, len(self._unusedBoxes)):
            if self._unusedBoxes[i] == val:
                boxindex = i
                break
        del self._unusedBoxes[boxindex]
        return

    def updateMainBoard(self, whoseTurn, choice):
        self._mainBoard[choice - 1] = whoseTurn
        self.removeChoice(choice)
