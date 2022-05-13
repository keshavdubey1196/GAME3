from dis import dis
import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
# Setting the color for the display
BLACK = (118, 115, 115)
WHITE = (239, 231, 200)
DISPLAY_COLOR = (28, 170, 156)
# COLOR = (255, 216, 253)
LINE_WIDTH = 15
LINE_COLOR = (23, 145, 135)
SQUARE_SIZE = 200
# LINE_COLOR = (255, 169, 253)
BOARD_ROWS = 3
BOARD_COLS = 3
PLAYER = 1
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4  # Space bw line and corner
GAME_OVER = False
display = pygame.display.set_mode((HEIGHT, WIDTH))  # Creates a window of specified size
pygame.display.set_caption("TIC TAC TOE")  # Title of the game(Display)0
display.fill(DISPLAY_COLOR)  # To give color to the window

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# Function to draw lines
def draw_lines():
    # 1st horizonta line
    pygame.draw.line(
        display, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH
    )
    # 2nd
    pygame.draw.line(
        display, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH
    )
    # 1st vertical line
    pygame.draw.line(
        display, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, WIDTH), LINE_WIDTH
    )
    # 2nd
    pygame.draw.line(
        display, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, WIDTH), LINE_WIDTH
    )


draw_lines()

# To assign a given value to any location of the matrix using this function
def mark_sq(row, col, player):
    board[row][col] = player


# To chcek if the board locations are available
def available_square(row, col):
    return board[row][col] == 0
    # return board[row][col] if board[row][col] == 0 else False


# To check if board full
def isBoard_full():
    for row in range(BOARD_ROWS):
        for cols in range(BOARD_COLS):
            if board[row][cols] == 0:
                return False
    return True


def draw_shapes():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    display,
                    WHITE,
                    (
                        int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                        int(row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    ),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )
                """
                To draw a circle.Args=== display,color,x&y pos,circle_rad,circle_width
                x--> starting position
                y--> ending position
                """
            elif board[row][col] == 2:
                pygame.draw.line(
                    display,
                    BLACK,
                    (
                        col * SQUARE_SIZE + SPACE,
                        row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                    ),
                    (
                        col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                        row * SQUARE_SIZE + SPACE,
                    ),
                    CROSS_WIDTH,
                )
                pygame.draw.line(
                    display,
                    BLACK,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                    (
                        col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                        row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                    ),
                    CROSS_WIDTH,
                )
                """
                To draw the Crosses
                """


def check_win(PLAYER):
    # Vertical win check
    for col in range(BOARD_COLS):
        if (
            board[0][col] == PLAYER
            and board[1][col] == PLAYER
            and board[2][col] == PLAYER
        ):
            draw_vertical_win_line(col, PLAYER)
            return True
    # horizontal win check
    for row in range(BOARD_ROWS):
        if (
            board[row][0] == PLAYER
            and board[row][1] == PLAYER
            and board[row][2] == PLAYER
        ):
            draw_horizontal_win_line(row, PLAYER)
            return True
    # Ascending win check
    if board[2][0] == PLAYER and board[1][1] == PLAYER and board[0][2] == PLAYER:
        draw_ascndg_diagnol(PLAYER)
        return True
    # Descending win check
    if board[0][0] == PLAYER and board[1][1] == PLAYER and board[2][2] == PLAYER:
        draw_dsndng_diagnol(PLAYER)
        return True
    return False


def draw_vertical_win_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    pygame.draw.line(display, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_win_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK

    pygame.draw.line(display, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_ascndg_diagnol(player):
    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK

    pygame.draw.line(display, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_dsndng_diagnol(player):
    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    pygame.draw.line(display, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    display.fill(DISPLAY_COLOR)
    draw_lines()
    PLAYER = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


# Main loop for the game:
while True:
    # This will hold the screen for time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # Checking for an input from the user
        if event.type == pygame.MOUSEBUTTONDOWN and not GAME_OVER:
            # To link our console board and our display board
            X = event.pos[0]  # x coordinate
            Y = event.pos[1]  # y coordinate
            # print(X, Y)

            click_row = int(Y // SQUARE_SIZE)
            click_col = int(X // SQUARE_SIZE)
            # print(click_row, click_col)
            if available_square(click_row, click_col):
                if PLAYER == 1:
                    mark_sq(click_row, click_col, 1)
                    if check_win(PLAYER):
                        GAME_OVER = True
                    PLAYER = 2
                elif PLAYER == 2:
                    mark_sq(click_row, click_col, 2)
                    if check_win(PLAYER):
                        GAME_OVER = True
                    PLAYER = 1
                draw_shapes()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                GAME_OVER = False

    pygame.display.update()  # To update the diplay with the given color
