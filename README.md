# Notakto


This programme implements the traditional Japanese board game Notakto.
This programme also checks for legal moves. If the users enters something illegal you should prompt them again.


Notakto is a tic-tac-toe variant. It is played across three 3 x 3 boards: Board A, board B and board C. Below is a standard Notakto board.

A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
6 7 8  6 7 8  6 7 8


There are two players: Player 1 and player 2. Player 1 starts first. Both players play the same piece: X.
E.g., let player 1 choose location 6 on board A, i.e., the user will enter A6.

A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
6 7 8  6 7 8  6 7 8
Player 1: A6
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
X 7 8  6 7 8  6 7 8
Player 2:


Each player takes turn placing an X on the board in a vacant space (a space not already occupied by an X).

A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
6 7 8  6 7 8  6 7 8
Player 1: A6
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
X 7 8  6 7 8  6 7 8
Player 2: A7
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
X X 8  6 7 8  6 7 8
Player 1:


If a board has three X in a row, column, or diagonal, the board is dead and it cannot be played anymore. It should not be displayed anymore.
E.g., In the board below, board A becomes dead and is not displayed anymore.

A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
6 7 8  6 7 8  6 7 8
Player 1: A6
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
X 7 8  6 7 8  6 7 8
Player 2: A7
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
X X 8  6 7 8  6 7 8
Player 1: A8
B      C
0 1 2  0 1 2
3 4 5  3 4 5
6 7 8  6 7 8
Player 2:


The game ends when all the boards contain three X in a row, column, or diagonal, at which point the player to have made the last move loses the game.
Unlike tic-tac-toe, there will always be a player who wins any game of Notakto.

A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
6 7 8  6 7 8  6 7 8
Player 1: A6
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
X 7 8  6 7 8  6 7 8
Player 2: A7
A      B      C
0 1 2  0 1 2  0 1 2
3 4 5  3 4 5  3 4 5
X X 8  6 7 8  6 7 8
Player 1: A8
B      C
0 1 2  0 1 2
3 4 5  3 4 5
6 7 8  6 7 8
Player 2: B0
B      C
X 1 2  0 1 2
3 4 5  3 4 5
6 7 8  6 7 8
Player 1: B4
B      C
X 1 2  0 1 2
3 X 5  3 4 5
6 7 8  6 7 8
Player 2: C0
B      C
X 1 2  X 1 2
3 X 5  3 4 5
6 7 8  6 7 8
Player 1: C4
B      C
X 1 2  X 1 2
3 X 5  3 X 5
6 7 8  6 7 8
Player 2: C8
B
X 1 2
3 X 5
6 7 8
Player 1: B8
Player 2 wins game
