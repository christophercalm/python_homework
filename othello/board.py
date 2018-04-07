#Othello Board Class

from square import *
from colors import *
class Board:

    def __init__(self):
        self.grid = [[Square() for h in range(8)] for k in range(8)]
        
        
    #def legalMoves():

    #def setUpBoard(self):
        #set up initial squares
        #self.grid[3][3].square.color = (black, False)
        #self.grid[4][4] = (black, False)
        #self.grid[3][4] = (white, False)
        #self.grid[3][4].isEmpty = False
        #self.grid[4][3].isEmpty = False
