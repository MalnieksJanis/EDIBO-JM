#libaries we need! important othervise progam won't work!
import pygame, sys
import numpy as np

# initializes pygame
pygame.init()


# CONSTANTS->> or everything we can take from here like color, size, width, height


WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 20
WIN_LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 10
CROSS_WIDTH = 20
SPACE = 55
# rgb: red green blue
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



# SCREEN

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'X and O' )
screen.fill( WHITE )


# CONSOLE BOARD

board = np.zeros( (BOARD_ROWS, BOARD_COLS) )


# FUNCTIONS
# function for line drawing where 1) whehe is screen 2) color 3) line position
def draw_lines():
	# 1 horizontal
	pygame.draw.line( screen, BLACK, (0, 200), (WIDTH, 200), LINE_WIDTH )
	# 2 horizontal
	pygame.draw.line( screen, BLACK, (0, 2 * 200), (WIDTH, 2 * 200), LINE_WIDTH )

	# 1 vertical
	pygame.draw.line( screen, BLACK, (200, 0), (200, HEIGHT), LINE_WIDTH )
	# 2 vertical
	pygame.draw.line( screen, BLACK, (2 * 200, 0), (2 * 200, HEIGHT), LINE_WIDTH )
# circle and x drawing where location is on x and y
def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, BLACK, (int( col * 200 + 200//2 ), int( row * 200 + 200//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, BLACK, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH )
				pygame.draw.line( screen, BLACK, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH )

def mark_square(row, col, player):
	board[row][col] = player

def available_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False

	return True

def check_win(player):
	# vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * 200 + 200//2

	if player == 1:
		color = BLACK
	elif player == 2:
		color = BLACK

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * 200 + 200//2

	if player == 1:
		color = BLACK
	elif player == 2:
		color = BLACK

	pygame.draw.line( screen, BLACK, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = BLACK
	elif player == 2:
		color = BLACK

	pygame.draw.line( screen, BLACK, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = BLACK
	elif player == 2:
		color = BLACK

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

def restart():
	screen.fill( WHITE )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

draw_lines()

# ---------
# VARIABLES
# ---------
player = 1
game_over = False

# --------
# MAINLOOP
# --------
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
# nodrošinam visu nepieciešamo, lai darbotos peles funkcijas
		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // 200)
			clicked_col = int(mouseX // 200)

			if available_square( clicked_row, clicked_col ):

				mark_square( clicked_row, clicked_col, player )
				if check_win( player ):
					game_over = True
				player = player % 2 + 1

				draw_figures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()