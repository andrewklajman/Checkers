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

    if 0 <= currentPosition[0] < BOARD_SIZE and 0 <= currentPosition[1] < BOARD_SIZE - 1:
        if BOARD[currentPosition[0] - 1][currentPosition[1] + 1] == BLANK:
            tmp.append ((currentPosition[0] - 1,currentPosition[1] + 1))
    if 0 <= currentPosition[0] < BOARD_SIZE and 0 < currentPosition[1] <= BOARD_SIZE - 1:
        if BOARD[currentPosition[0] - 1][currentPosition[1] - 1] == BLANK:
            tmp.append ((currentPosition[0] - 1,currentPosition[1] - 1))

    if 0 <= currentPosition[0] < BOARD_SIZE - 1 and 0 <= currentPosition[1] < BOARD_SIZE - 2:
        if BOARD[currentPosition[0] - 1][currentPosition[1] + 1] == opposingPlayer() and BOARD[currentPosition[0] - 2][currentPosition[1] + 2] == BLANK:
            tmp.append ((currentPosition[0] - 1,currentPosition[1] + 1))
        
    return tmp
                

 


    
BOARD = initBoard()
BOARD[5][4] = NAUGHT
BOARD[4][2] = NAUGHT
BOARD[4][7] = NAUGHT
BOARD[3][5] = CROSS
BOARD[3][3] = CROSS
printBoard()
print()



print(possibleMoves((4,2)))









