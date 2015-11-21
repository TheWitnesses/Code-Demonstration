import random
import sys
import time

from pygame.locals import *

from TicTacToeUI import *
from TicTacToeBoard import *

board = Board()
visualBoard = VisualBoard()
visualBoard._showScreen.blit(visualBoard._textSurfaceObjPlayerChoice, visualBoard._textRectPlayerChoice)
# ...
class Game:
    def getNextEvent(self, board):
        cancelGame = False
        validChoice = False
        choice = None
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                cancelGame = True
            elif event.type == KEYDOWN:
                xChoice = event.key - board._keyOffset
                choice = xChoice
                for i in range(0, len(board._unusedBoxes)):
                    if board._unusedBoxes[i] == choice:
                        validChoice= True
        return cancelGame, validChoice, choice

    def checkDraw(self, board):
        if len(board._unusedBoxes) == 0 and not board._gameOver:
                    if not board._winner:
                        visualBoard._showScreen.blit(visualBoard._textSurfaceObjPlayerChoiceb, visualBoard._textRectPlayerChoice)
                        visualBoard._showScreen.blit(visualBoard._textSurfaceObjDraw, visualBoard._textRectDraw)
                    board._gameOver = True

    def processGameChoice(self, whoseTurn, choice, board):
        board.updateMainBoard(whoseTurn, choice)
        visualBoard.place(whoseTurn, choice)
        board._gameOver = board.checkWin(whoseTurn, visualBoard.displayWin)


    def run(self):
        cancelGame = False
        while not board._gameOver and not cancelGame:

            cancelGame, validChoice, choice = self.getNextEvent(board)

            if validChoice:
                    game.processGameChoice('X', choice, board)
                    game.checkDraw(board)
                    pygame.display.update()
                    time.sleep(1)

                    if not board._gameOver:
                        choice = random.choice(board._unusedBoxes)
                        game.processGameChoice('O', choice, board)

            pygame.display.update() # if put in variable, will delay updating the screen

        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game() # Creates new instance of the class
    game.run()
