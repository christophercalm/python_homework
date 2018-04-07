#pygame tutorial
import pygame



pygame.init()

#dimensions
display_width = 900
display_height = 600

#startx, starty
x = (display_width * .0)
y = (display_height * .0) #top left

#colors
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Othello")
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render("Othello", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = gameDisplay.get_rect().centerx
#images
boardImg = pygame.image.load('reversiBoard.png')

#Othello piece class

class Square:

	def __init__(self):
		self.isEmpty = True
		self.color = null

	def flip():
		if self.color == white:
			self.color = black
		elif self.color == black:
			self.color = black
			
#Othello Board Class
class Board:

	def __init__(self):
		self.name = name
		self.grid = [ [Square() for n in range(8)] for n in range(8)]
		
		
	#def legalMoves():

	def setUpBoard():
		#set up initial squares
		self.grid[3][3].color = black
		self.grid[3][3].isEmpty = False
		self.grid[4][4].color = black
		self.grid[4][4].isEmpty = False
		self.grid[3][4].color = white
		self.grid[3][4].isEmpty = False
		self.grid[4][3].color = white
		self.grid[4][3].isEmpty = False
	
			
		  

def drawBoard(x,y):
	gameDisplay.blit(boardImg, (x,y)) #draws board
def drawPiece(xPos, yPos, color):
        pygame.draw.circle(gameBoard, color, (xPos, yPos), 37) #radius is half of square

#set up inital board
#gameBoard = Board()
#gameBoard.setUpBoard()

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
	while not done:
	
		for event in pygame.event.get(): #get all events
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONUP: #clicking on sprites
				pos = pygame.mouse.get_pos()

				# get a list of all sprites that are under the mouse cursor
				#clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
				# do something with the clicked sprites...

		gameDisplay.fill(black) # this has to go first
		drawBoard(x,y)
		drawPiece(0,0, white)

		pygame.display.update() #use this or flip

		clock.tick(30) # 30fps, moves program along

#gameIntro()
gameLoop()
pygame.quit() 
quit()
		
