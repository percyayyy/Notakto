remaining = ['A', 'B', 'C']
model = [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]
board = [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]

for i in range(len(remaining) - 1):
    print(remaining[i], end = '      ')
print(remaining[-1])
for i in range(len(board)):
    for j in range(2):
        for k in range(2):
            print(board[j][i][k], end = ' ')
        print(board[j][i][2], end = '  ')
    for k in range(2):
        print(board[2][i][k], end = ' ')
    print(board[2][i][2])

turn = 0
while True:
    win = 0
    turn += 1
    while True:
        checkDouble = 0
        if turn % 2 != 0:
            player1 = input('Player 1: ')
            if (len(player1) == 2) and (remaining.count(player1[0]) > 0) and (player1[1].isdecimal() is True) and (player1[1] != '9'):
                for i in range(3):
                    for j in range(3):
                        if (str(board[remaining.index(player1[0])][i][j]) == 'X') and (str(model[remaining.index(player1[0])][i][j]) == player1[1]):
                            checkDouble += 1
            if (len(player1) == 2) and (remaining.count(player1[0]) > 0) and (player1[1].isdecimal() is True) and (checkDouble == 0) and (player1[1] != '9'):
                break
            else:
                print('Invalid move, please input again')
        else:
            player2 = input('Player 2: ')
            if (len(player1) == 2) and (remaining.count(player1[0]) > 0) and (player1[1].isdecimal() is True) and (player1[1] != '9'):
                for i in range(3):
                    for j in range(3):
                        if (str(board[remaining.index(player2[0])][i][j]) == 'X') and (str(model[remaining.index(player2[0])][i][j]) == player2[1]):
                            checkDouble += 1
            if (len(player2) == 2) and (remaining.count(player2[0]) > 0) and (player2[1].isdecimal() is True) and (checkDouble == 0) and (player1[1] != '9'):
                break
            else:
                print('Invalid move, please input again')

    if turn % 2 != 0:
        whichBoard = remaining.index(player1[0])
        for i in range(3):
            for j in range(3):
                if str(board[whichBoard][i][j]) == player1[1]:
                    board[whichBoard][i][j] = 'X'
    else:
        whichBoard = remaining.index(player2[0])
        for i in range(3):
            for j in range(3):
                if str(board[whichBoard][i][j]) == player2[1]:
                    board[whichBoard][i][j] = 'X'

    for i in range(len(board)):
        for j in range(3):
            if (board[i][j].count('X') == 3):
                win += 1
            if (board[i][0][j] == board[i][1][j]) and (board[i][1][j] == board[i][2][j]) and (board[i][0][j] == 'X'):
                win += 1
    for i in range(len(board)):
        if (board[i][0][0] == board[i][1][1]) and (board[i][0][0] == board[i][2][2]) and (board[i][0][0] == 'X'):
            win += 1
        if (board[i][0][2] == board[i][1][1]) and (board[i][0][2] == board[i][2][0]) and (board[i][0][2] == 'X'):
            win += 1

    if (win > 0) and (len(remaining) == 1):
        if turn % 2 != 0:
            print('Player 2 wins game')
            break
        else:
            print('Player 1 wins game')
            break
    elif win > 0:
        if turn % 2 != 0:
            del remaining[whichBoard]
            del board[whichBoard]
        else:
            del remaining[whichBoard]
            del board[whichBoard]

    for i in range(len(remaining) - 1):
        print(remaining[i], end = '      ')
    print(remaining[-1])
    for i in range(3):
        for j in range(len(remaining) - 1):
            for k in range(2):
                print(board[j][i][k], end = ' ')
            print(board[j][i][2], end = '  ')
        for k in range(2):
            print(board[-1][i][k], end = ' ')
        print(board[-1][i][2])
