import pygame

BOARD_SIZE = 5
BLANK = '-'
NAUGHT = 'O'
CROSS = 'X'
BOARD = []
currentPlayer = NAUGHT

RES = 400
SIZE = 8
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
DIM = int(RES/SIZE)

pygame.init()
gd = pygame.display.set_mode((RES,RES))
board = {}
mouseUp = 0
mouseDown = 0
prevPress = 0
prevPos = 0

def initBoard():
    global board
    gd.fill(BLACK)
    [pygame.draw.rect(gd, WHITE, [c,r,DIM,DIM]) for r in range(0,RES, DIM * 2) for c in range(0,RES, DIM * 2)]
    [pygame.draw.rect(gd, WHITE, [c+DIM,r+DIM,DIM,DIM]) for r in range(0,RES, DIM * 2) for c in range(0,RES, DIM * 2)]
    board = {(i,0):drawNaught((i,0),RED) for i in range(0,SIZE,2)}
    board = {**board,**{(i,1):drawNaught((i,1),RED) for i in range(1,SIZE + 1,2)}}
    board = {**board,**{(i,SIZE - 2):drawNaught((i,SIZE - 2),BLUE) for i in range(0,SIZE,2)}}
    board = {**board,**{(i,SIZE - 1):drawNaught((i,SIZE - 1),BLUE) for i in range(1,SIZE + 1,2)}}

def drawNaught(pos, color):
    pygame.draw.circle(gd, color, (int((pos[0] + 0.5) * DIM), int((pos[1] + 0.5) * DIM)), int(DIM * 0.4))
    return color

def possiblePosition(pos):
    tmp = []
    if pos in board:
        if board[pos] == RED:
            if (pos[0] + 1, pos[1] + 1) not in board:
                tmp.append((pos[0] + 1, pos[1] + 1))
            if (pos[0] - 1, pos[1] + 1) not in board:
                tmp.append((pos[0] - 1, pos[1] + 1))

        if board[pos] == BLUE:
            if (pos[0] + 1, pos[1] - 1) not in board:
                tmp.append((pos[0] + 1, pos[1] - 1))
            if (pos[0] - 1, pos[1] - 1) not in board:
                tmp.append((pos[0] - 1, pos[1] - 1))
    return tmp
                
def drawBoard():
    gd.fill(BLACK)
    [pygame.draw.rect(gd, WHITE, [c,r,DIM,DIM]) for r in range(0,RES, DIM * 2) for c in range(0,RES, DIM * 2)]
    [pygame.draw.rect(gd, WHITE, [c+DIM,r+DIM,DIM,DIM]) for r in range(0,RES, DIM * 2) for c in range(0,RES, DIM * 2)]
    for pos,col in board.items():
        drawNaught(pos, col)

initBoard()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pos = (int(pygame.mouse.get_pos()[0]/DIM),int(pygame.mouse.get_pos()[1]/DIM))
   
    if pygame.mouse.get_pressed()[0] == 1:
        [drawNaught(p,GREEN) for p in possiblePosition(pos)]
    else:
        drawBoard()
        
    if pygame.mouse.get_pressed()[0] == 1:
        if prevPress != 1:
            prevPos = pos
        prevPress = 1
        
    elif pygame.mouse.get_pressed()[0] == 0 and prevPress == 1 and pos != prevPos and pos in possiblePosition(prevPos):
        board[pos] = board[prevPos]
        del board[prevPos]
        drawBoard()
        prevPress = 0
    
    pygame.display.update()
