import pygame
RES = 400
SIZE = 8
DIM = int(RES/SIZE)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PLAYER = RED

pygame.init()
gd = pygame.display.set_mode((RES,RES))
clock = pygame.time.Clock()
board = {}
mPressedPrev = 0
potMoves = []
potGridPos = []
selection_first = 0
selection_last = 0

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def initBoard():
    global board
    board = {(i,0):RED for i in range(0,SIZE,2)}
    board = {**board,**{(i,1):RED for i in range(1,SIZE + 1,2)}}
    board = {**board,**{(i,SIZE - 2):BLUE for i in range(0,SIZE,2)}}
    board = {**board,**{(i,SIZE - 1):BLUE for i in range(1,SIZE + 1,2)}}
    drawBoard()

def drawNaught(pos, color):
    pygame.draw.circle(gd, color, (int((pos[0] + 0.5) * DIM), int((pos[1] + 0.5) * DIM)), int(DIM * 0.4))

def possiblePosition(pos):
    tmp = []
    if pos in board:
        if board[pos] == RED:
            if (pos[0] + 1, pos[1] + 1) not in board:
                tmp.append((pos[0] + 1, pos[1] + 1))
            if (pos[0] - 1, pos[1] + 1) not in board:
                tmp.append((pos[0] - 1, pos[1] + 1))
            if (pos[0] + 1,pos[1] + 1) in board:
                if board[(pos[0] + 1,pos[1] + 1)] == BLUE and (pos[0] + 2, pos[1] + 2) not in board:
                    tmp.append((pos[0] + 2, pos[1] + 2))
            if (pos[0] - 1,pos[1] + 1) in board:
                if board[(pos[0] - 1,pos[1] + 1)] == BLUE and (pos[0] - 2, pos[1] + 2) not in board:
                    tmp.append((pos[0] - 2, pos[1] + 2))
        if board[pos] == BLUE:
            if (pos[0] + 1, pos[1] - 1) not in board:
                tmp.append((pos[0] + 1, pos[1] - 1))
            if (pos[0] - 1, pos[1] - 1) not in board:
                tmp.append((pos[0] - 1, pos[1] - 1))
            if (pos[0] + 1,pos[1] - 1) in board:
                if board[(pos[0] + 1,pos[1] - 1)] == RED and (pos[0] + 2, pos[1] - 2) not in board:
                    tmp.append((pos[0] + 2, pos[1] - 2))
            if (pos[0] - 1,pos[1] - 1) in board:
                if board[(pos[0] - 1,pos[1] - 1)] == RED and (pos[0] - 2, pos[1] - 2) not in board:
                    tmp.append((pos[0] - 2, pos[1] - 2))
    return tmp
                
def drawBoard():
    gd.fill(BLACK)
    [pygame.draw.rect(gd, WHITE, [c,r,DIM,DIM]) for r in range(0,RES, DIM * 2) for c in range(0,RES, DIM * 2)]
    [pygame.draw.rect(gd, WHITE, [c+DIM,r+DIM,DIM,DIM]) for r in range(0,RES, DIM * 2) for c in range(0,RES, DIM * 2)]
    for pos,col in board.items():
        drawNaught(pos, col)

def switchPlayer():
    global PLAYER
    if PLAYER == RED:
        PLAYER = BLUE
    else:
        PLAYER = RED
    


initBoard()
while True:
    checkQuit()
    gridPos = (int(pygame.mouse.get_pos()[0]/DIM),int(pygame.mouse.get_pos()[1]/DIM))
    mPressed = (pygame.mouse.get_pressed()[0] == 1)

    if mPressed and not(mPressedPrev):
        selection_first = gridPos
    if not(mPressed) and mPressedPrev:
        selection_last = gridPos

    if selection_first in board and board[selection_first] == PLAYER and selection_last in potMoves:
        if abs(selection_first[0] - selection_last[0]) == 1:
            board[selection_last] = board[selection_first]
            del board[selection_first]
            switchPlayer()
        if abs(selection_first[0] - selection_last[0]) == 2:
            board[selection_last] = board[selection_first]
            del board[((selection_first[0] + selection_last[0])/2, (selection_first[1] + selection_last[1])/2)]
            del board[selection_first]
            switchPlayer()

    if mPressed and selection_first in board and board[selection_first] == PLAYER:
        potMoves = possiblePosition(selection_first)
    else:
        potMoves = []

    mPressedPrev = mPressed
    drawBoard()
    [drawNaught(p,GREEN) for p in potMoves]
    pygame.display.update()
    clock.tick(60)
