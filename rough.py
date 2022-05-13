import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
# Setting the color for the display
BLACK = (0, 0, 0)
COLOR = (28, 170, 156)
# COLOR = (255, 216, 253)
LINE_WIDTH = 15
LINE_COLOR = (23, 145, 135)
# LINE_COLOR = (255, 169, 253)
BOARD_ROWS = 3
BOARD_COLS = 3
display = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates a window of specified size
pygame.display.set_caption("TIC TAC TOE")  # Title of the game(Display)0
display.fill(COLOR)  # To give color to the window

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# Function to draw lines
def draw_lines():
    # 1st horizonta line
    pygame.draw.line(display, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2nd
    pygame.draw.line(display, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # 1st vertical line
    pygame.draw.line(display, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2nd
    pygame.draw.line(display, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()

# To assign a given value to any location of the matrix using this function
def mark_sq(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0
    # return board[row][col] if board[row][col] == 0 else False


def isBoard_full():
    for row in range(BOARD_ROWS):
        for cols in range(BOARD_COLS):
            if board[row][cols] == 0:
                return False
    return True


# Main loop for the game:
while True:
    # This will hold the screen for time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # Checking for an input from the user
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # To link our console board and our display board
            X = event.pos[0]  # x coordinate
            Y = event.pos[1]  # y coordinate
            print(X, Y)

            click_row = int(Y // 200)
            click_col = int(X // 200)
            # print(click_row, click_col)

    pygame.display.update()  # To update the diplay with the given color
