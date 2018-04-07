#pygame tutorial
import pygame
from board import *
from square import *

pygame.init()

#dimensions
display_width = 900
display_height = 600
block_size = 75
radius = 37

#colors
black = (0,0,0)
white = (255,255,255)
green = (0,144,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Othello")
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render("Othello", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = gameDisplay.get_rect().centerx
#images
boardImg = pygame.image.load('reversiBoard.png')


def drawPiece(xPos, yPos, color):
	pygame.draw.circle(gameDisplay, color, (xPos*block_size+radius,yPos*block_size+radius), 37,0) #radius is half of square	

#set up inital board
gameBoard = Board()
#gameBoard.setUpBoard()


def getRect(x,y):
    posX = x // block_size
    posY = y // block_size
    return (posX,posY)

def drawBoard():
        for row in range(8):
                for col in range(8):
                        rect = (row * block_size, col * block_size, block_size, block_size)
                        rectangle = pygame.draw.rect(gameDisplay, black, rect,2)
    #gameDisplay.blit(boardImg, (x,y)) #draws board

def drawGrid(x,y):
        for row in range(8):
                for col in range(8):
                        print(hex(id(gameBoard.grid[x][y])))
                        print(gameBoard.grid[x][y].isEmpty)
                        if gameBoard.grid[x][y].isEmpty==False:
                                drawPiece(x,y, gameBoard.grid[x][y].color)
                        #pygame.draw.circle(gameDisplay,white,(getRect(posX,posY)),37, 0)
                       


#intro screen for game
def gameIntro():
	
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			pressed = pygame.key.get_pressed()
			#move to gameloop if press return
			if pressed[pygame.K_RETURN]:
				intro = False

		gameDisplay.fill(black)
		largeText = pygame.font.Font('freesansbold.ttf',115)
		#display text
		pygame.display.update()
		clock.tick(1)


def gameLoop():
        
	done = False
	gameDisplay.fill(green) # this has to go first
	drawBoard()
	while not done:
                
		for event in pygame.event.get(): #get all events
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN: #clicking on sprites
				posX, posY = pygame.mouse.get_pos()
				posGridX, posGridY, = getRect(posX,posY)
				print(str(posGridX)+","+str(posGridY))				
				gameBoard.grid[posGridX][posGridY].isEmpty = False
				gameBoard.grid[posGridX][posGridY].color = white
				print(gameBoard.grid[posGridX][posGridY].isEmpty)

				drawGrid(posGridX,posGridY)
				
				
				
				#rint(posX, posY)
								#drawPiece(posX, posY , white)

                                
				print(getRect(posX,posY))

				# get a list of all sprites that are under the mouse cursor
				#clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
				# do something with the clicked sprites...
		

        
		pygame.display.update() #use this or flip

		clock.tick(30) # 30fps, moves program along
#gameIntro()
gameLoop()
getRect(76,2)
pygame.quit() 
quit()
		
