##Adding some additional informaiton
BOARD_SIZE = 8
BLANK = '-'
NAUGHT = 'O'
CROSS = 'X'
BOARD = []
currentPlayer = NAUGHT

def printBoard():
    print('  ' + ''.join([str(i) for i in range(BOARD_SIZE)]))
    [print(str(r) + ' ' + ''.join(BOARD[r])) for r in range(BOARD_SIZE)]

def initBoard():
    return [[BLANK] * BOARD_SIZE for r in range(BOARD_SIZE)]

def currentPositions(player):
    return [(r,c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if BOARD[r][c] == player]

def possibleMoves(currentPosition):
    tmp = []
    if currentPosition[0] - 1 != -1:
        if currentPosition[1] + 1 != BOARD_SIZE:
            if BOARD[currentPosition[0] - 1][currentPosition[1] + 1] == BLANK:
                tmp.append((currentPosition[0] - 1, currentPosition[1] + 1))
    if currentPosition[0] - 1 != -1:
        if currentPosition[1] - 1 != -1:
            if BOARD[currentPosition[0] - 1][currentPosition[1] - 1] == BLANK:
                tmp.append((currentPosition[0] - 1, currentPosition[1] - 1))
    return tmp
                

 


    
BOARD = initBoard()
BOARD[4][4] = NAUGHT
BOARD[4][6] = NAUGHT
BOARD[4][7] = NAUGHT
BOARD[3][5] = CROSS
BOARD[3][3] = CROSS
printBoard()
print()



print(possibleMoves((4,4)))









