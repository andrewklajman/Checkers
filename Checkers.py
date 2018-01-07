BOARD_SIZE = 8
BLANK = '.'
NAUGHT = 'O'
CROSS = 'X'
INVALID_MOVE = 'INVALID MOVE'
BOARD = []

def printBoard():
    print('  ' + ''.join([str(i) for i in range(BOARD_SIZE)]))
    for r in range(BOARD_SIZE):
        print(str(r) + ' ' + ''.join(BOARD[r]))
    print()

def movePiece(curPos, proPos):
    if BOARD[curPos[0]][curPos[1]] == NAUGHT:
        playerPerspective = 1
    elif BOARD[curPos[0]][curPos[1]] == CROSS:
        playerPerspective = -1
    else:
        return INVALID_MOVE

    if ((curPos[0] - proPos[0]) == 1 or (curPos[0] - proPos[0]) == - 1) and (curPos[1] - proPos[1]) == 1 * playerPerspective and BOARD[proPos[0]][proPos[1]] == BLANK:
        BOARD[curPos[0]][curPos[1]] = BLANK
        if playerPerspective == 1:
            BOARD[proPos[0]][proPos[1]] = NAUGHT
        elif playerPerspective == -1:
            BOARD[proPos[0]][proPos[1]] = CROSS

    elif if ((curPos[0] - proPos[0]) == 2 or (curPos[0] - proPos[0]) == - 2) and (curPos[1] - proPos[1]) == 2 * playerPerspective \
                             and (BOARD[proPos[0] - 1][proPos[1] - 1] == BLANK):
        BOARD[curPos[0]][curPos[1]] = BLANK
        if playerPerspective == 1:
            BOARD[proPos[0]][proPos[1]] = NAUGHT
        elif playerPerspective == -1:
            BOARD[proPos[0]][proPos[1]] = CROSS






            
    
for r in range(BOARD_SIZE):
    tmp = []
    for c in range(BOARD_SIZE):
            tmp.append(BLANK)
    BOARD.append(tmp)

BOARD[4][4] = NAUGHT
BOARD[3][5] = CROSS

printBoard()
    
##movePiece((3,5),(4,6))
##movePiece((4,4),(3,3))

printBoard()
