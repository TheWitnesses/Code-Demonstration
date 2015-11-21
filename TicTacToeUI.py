import pygame
from TicTacToeBoard import *

class VisualBoard:
    def __init__(self): # Starts the game
        self._start = pygame.init()
        self._askChoice = 'Put X on board. Use number keys. Press Esc to quit.'
        self._showScreen = pygame.display.set_mode((864, 720))
        self._showCaption = pygame.display.set_caption('Have fun with Tic Tac Toe!')
        self._update = pygame.display.update()

        # Color
        self._white = (255, 255, 255)
        self._red = (255, 0, 0)
        self._gray = (126, 126, 126)
        self._orange = (207, 118, 32)
        self._black = (0, 0, 0)
        self._blue = (0, 0, 255)

         # Fonts
        self._fontObj = pygame.font.Font('freesansbold.ttf', 50)
        self._fontObj26 = pygame.font.Font('freesansbold.ttf', 26)
        self._fontObj150 = pygame.font.Font('freesansbold.ttf', 150)

        self._xFontCenter = (432, 360)
        self._oFontCenter = (648, 144)
        self._winFontCenter =  (432, 684)

        #Get User Input
        self._textSurfaceObjPlayerChoice = self._fontObj26.render(self._askChoice, False ,self._orange) # Orange
        self._textSurfaceObjPlayerChoiceb = self._fontObj26.render(self._askChoice, False, self._black) # Black
        self._textRectPlayerChoice = self._textSurfaceObjPlayerChoice.get_rect()
        self._textRectPlayerChoice.center = self._winFontCenter

        #Declares Winner for X
        self._textSurfaceObjWinnerX = self._fontObj26.render('X Wins!', True, self._blue) # Blue
        self._textRectWinnerX = self._textSurfaceObjWinnerX.get_rect()
        self._textRectWinnerX.center = self._winFontCenter

        #Declares Winner for O
        self._textSurfaceObjWinnerO= self._fontObj26.render('O Wins!', True, self._blue) # Blue
        self._textRectWinnerO = self._textSurfaceObjWinnerO.get_rect()
        self._textRectWinnerO.center = self._winFontCenter

        self._textSurfaceObjDraw= self._fontObj26.render('No Winner!', True, self._blue) #Blue
        self._textRectDraw = self._textSurfaceObjDraw.get_rect()
        self._textRectDraw.center = self._winFontCenter

        # Center spacing for small gray numbers
        self._columns = [216, 432, 648]
        self._rows = [144, 360, 576]
        self._Centers = [(col, row)
                   for row in self._rows
                       for col in self._columns]

        self._bigColumns = [166, 381, 598]
        self._bigRows = [69, 285, 501]
        self._bigCenters = [(col, row)
                   for row in self._bigRows
                       for col in self._bigColumns]

        self._numPics = [] # Array holding light gray numbers
        self._numBlanks = [] # Array holding black numbers to erase gray numbers
        self._numRect = [] # Array holding rectangles size of the numbers

        #num = 1
        for num in range(0, 9):
            self._grayNumber = self._fontObj.render((str(num + 1)), False, self._gray) # Gray

            self._numPics.append(self._grayNumber)

            self._blackNumber = self._fontObj.render((str(num + 1)), False, self._black) # Black
            self._numBlanks.append(self._blackNumber)

            self._numberSize = self._grayNumber.get_rect()
            self._numberSize.center = self._Centers[num]
            self._numRect.append(self._numberSize)

        for num in range(0, 9):
            self._showScreen.blit(self._numPics[num], self._numRect[num])

        pygame.draw.rect(self._showScreen, self._white, (300, 72, 72, 576)) #White
        pygame.draw.rect(self._showScreen, self._white, (503, 72, 72, 576))
        pygame.draw.rect(self._showScreen, self._white, (144, 432, 576, 72))
        pygame.draw.rect(self._showScreen, self._white, (144, 216, 576, 72))

    def displayWin(self, val):
        self._showScreen.blit(self._textSurfaceObjPlayerChoiceb, self._textRectPlayerChoice)
        if val == "O":
                    self._showScreen.blit(self._textSurfaceObjWinnerO, self._textRectWinnerO)
        elif val == "X":
                    self._showScreen.blit(self._textSurfaceObjWinnerX, self._textRectWinnerX)

    def createPlayObj(self, player, center):
        textObj150 = self._fontObj150.render(player, True, self._red)
        textRectObj150 = textObj150.get_rect()
        textRectObj150.center = center
        return textObj150

    def place(self, player, pick):
        if player == 'X':
            center = self._xFontCenter
        else:
            center = self._oFontCenter
        boxindex = -1
        play = self.createPlayObj(player, center)
        self._showScreen.blit(self._numBlanks[pick - 1], self._numRect[pick - 1])
        self._showScreen.blit(play, self._bigCenters[pick - 1]) # 166, 69
