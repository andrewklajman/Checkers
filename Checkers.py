##Adding some additional informaiton
BOARD_SIZE = 5
BLANK = '-'
NAUGHT = 'O'
CROSS = 'X'
BOARD = []
currentPlayer = NAUGHT

def printBoard():
    print('  ' + ''.join([str(i) for i in range(BOARD_SIZE)]))
    [print(str(r) + ' ' + ''.join(BOARD[r])) for r in range(BOARD_SIZE)]

def initBoard():
    tmp = [[BLANK] * BOARD_SIZE for r in range(BOARD_SIZE)]
    for i in range(-1,BOARD_SIZE,2):
        if i > 0:
            tmp[0][i] = CROSS
    for i in range(0,BOARD_SIZE,2):
            tmp[1][i] = CROSS
    for i in range(-1,BOARD_SIZE,2):
        if i > 0:
            tmp[BOARD_SIZE - 2][i] = NAUGHT
    for i in range(0,BOARD_SIZE,2):
            tmp[BOARD_SIZE - 1][i] = NAUGHT
    return tmp

def currentPositions(player):
    return [(r,c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if BOARD[r][c] == player]

def possibleMoves(currentPosition):
    tmp = []
    
    if BOARD[currentPosition[0]][currentPosition[1]] == NAUGHT:
        if 1 <= currentPosition[0] <= BOARD_SIZE - 1 and 0 <= currentPosition[1] <= BOARD_SIZE - 2:
            if BOARD[currentPosition[0] - 1][currentPosition[1] + 1] == BLANK:
                tmp.append ((currentPosition[0] - 1,currentPosition[1] + 1))
        if 1 <= currentPosition[0] <= BOARD_SIZE - 1 and 1 <= currentPosition[1] <= BOARD_SIZE - 1:
            if BOARD[currentPosition[0] - 1][currentPosition[1] - 1] == BLANK:
                tmp.append ((currentPosition[0] - 1,currentPosition[1] - 1))
        if 2 <= currentPosition[0] <= BOARD_SIZE - 1 and 0 <= currentPosition[1] <= BOARD_SIZE - 3:
            if BOARD[currentPosition[0] - 1][currentPosition[1] + 1] == CROSS and BOARD[currentPosition[0] - 2][currentPosition[1] + 2] == BLANK:
                tmp.append ((currentPosition[0] - 2,currentPosition[1] + 2))
        if 2 <= currentPosition[0] <= BOARD_SIZE - 1 and 2 <= currentPosition[1] <= BOARD_SIZE - 1:
            if BOARD[currentPosition[0] - 1][currentPosition[1] - 1] == CROSS and BOARD[currentPosition[0] - 2][currentPosition[1] - 2] == BLANK:
                tmp.append ((currentPosition[0] - 2,currentPosition[1] - 2))

    if BOARD[currentPosition[0]][currentPosition[1]] == CROSS:
        if 0 <= currentPosition[0] <= BOARD_SIZE - 1 and 0 <= currentPosition[1] <= BOARD_SIZE - 2:
            if BOARD[currentPosition[0] + 1][currentPosition[1] + 1] == BLANK:
                tmp.append ((currentPosition[0] + 1,currentPosition[1] + 1))
        if 0 <= currentPosition[0] <= BOARD_SIZE - 1 and 1 <= currentPosition[1] <= BOARD_SIZE - 1:
            if BOARD[currentPosition[0] + 1][currentPosition[1] - 1] == BLANK:
                tmp.append ((currentPosition[0] + 1,currentPosition[1] - 1))
        if 0 <= currentPosition[0] <= BOARD_SIZE - 3 and 0 <= currentPosition[1] <= BOARD_SIZE - 3:
            if BOARD[currentPosition[0] + 1][currentPosition[1] + 1] == NAUGHT and BOARD[currentPosition[0] - 2][currentPosition[1] + 2] == BLANK:
                tmp.append ((currentPosition[0] + 2,currentPosition[1] + 2))
        if 0 <= currentPosition[0] <= BOARD_SIZE - 3 and 2 <= currentPosition[1] <= BOARD_SIZE - 1:
            if BOARD[currentPosition[0] + 1][currentPosition[1] - 1] == NAUGHT and BOARD[currentPosition[0] - 2][currentPosition[1] - 2] == BLANK:
                tmp.append ((currentPosition[0] + 2,currentPosition[1] - 2))

    return tmp
                
def movePiece(currentPosition, proposedPosition):
    BOARD[proposedPosition[0]][proposedPosition[1]] = BOARD[currentPosition[0]][currentPosition[1]]
    BOARD[currentPosition[0]][currentPosition[1]]   = BLANK

    print(abs(proposedPosition[0] - currentPosition[0]))
    if abs(proposedPosition[0] - currentPosition[0]) == 2:
        BOARD[int((currentPosition[0] + proposedPosition[0])/2)][int((currentPosition[1] + proposedPosition[1])/2)] = BLANK
    
BOARD = initBoard()

printBoard()
print()





























  








