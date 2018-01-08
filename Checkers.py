##Adding some additional informaiton
BOARD_SIZE = 8
BLANK = '-'
NAUGHT = 'O'
CROSS = 'X'
INVALID_MOVE = 'INVALID MOVE'
BOARD = []

currentPlayer = NAUGHT

def printBoard():
    print('  ' + ''.join([str(i) for i in range(BOARD_SIZE)]))
    for r in range(BOARD_SIZE):
        print(str(r) + ' ' + ''.join(BOARD[r]))
    print()

def potentialMoves(CurR,CurC):
    tmp = []

    if BOARD[CurR - 1 * orient][CurC - 1] == BLANK:
        tmp.append((CurR - 1 * orient,CurC - 1))
    if BOARD[CurR - 1 * orient][CurC + 1] == BLANK:
        tmp.append((CurR - 1 * orient,CurC + 1))

    if 0 <= CurR - 1 * orient < BOARD_SIZE:
        if 0 <= CurC + 2 < BOARD_SIZE:
            if BOARD[CurR - 2 * orient][CurC + 2] == BLANK and BOARD[CurR - 1 * orient][CurC + 1] == opposingPlayer(currentPlayer):
                tmp.append((CurR - 2 * orient,CurC + 2))
        if 0 <= CurC - 2 < BOARD_SIZE:
            if BOARD[CurR - 2 * orient][CurC - 2] == BLANK and BOARD[CurR - 1 * orient][CurC - 1] == opposingPlayer(currentPlayer):
                tmp.append((CurR - 2 * orient,CurC - 2))

    return tmp

def opposingPlayer(player):
    if player == NAUGHT:
        return CROSS
    return NAUGHT

    

def initBoard():
    for r in range(BOARD_SIZE):
        tmp = []
        for c in range(BOARD_SIZE):
                tmp.append(BLANK)
        BOARD.append(tmp)


initBoard()
BOARD[4][4] = NAUGHT
BOARD[4][6] = NAUGHT
BOARD[3][5] = CROSS


if currentPlayer == CROSS:
    orient = -1
else:
    orient = 1

cpos = (4,6)
ppos = (2,4)
print(ppos in potentialMoves(4,6))

if abs(ppos[0] - cpos[0]) == 2:
    BOARD[cpos[0] - 1 * orient][abs(cpos[1] - ppos[1] + 1)] = BLANK
    print


printBoard()


 
