# Step 1, create rows and columns
EMPTY = ""

chessboard = [[EMPTY for i in range(8)] for j in range(8)]

# Print the chessboard
#for row in chessboard:
#    print(row)

# Fill the chessboard with alternating black and white squares
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chessboard[i][j] = '■'  # Black squares represented by filled blocks
        else:
            chessboard[i][j] = ' '   # White squares represented by empty space

# Place chess pieces on the board
chessboard[0] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']  # Black back rank
chessboard[1] = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']  # Black pawns

chessboard[7] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']  # White back rank
chessboard[6] = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']  # White pawns

# Print the chessboard
for row in chessboard:
    print(' '.join(row))

r = int(input("Enter the row of the piece to move: "))
c = int(input("Enter the column of the piece to move: "))

if chessboard[r][c] == '♙':
    dr = int(input("Enter the row to move the piece to: "))
    dc = int(input("Enter the column to move the piece to: "))

    chessboard[dr][dc] = '♙'
    if r % 2 == 0:
        if c % 2 == 0:
            chessboard[r][c] = '■'
        else:
            chessboard[r][c] = ' '
    else:
        if c % 2 == 0:
            chessboard[r][c] = ' '
        else:
            chessboard[r][c] = '■'

# Print the chessboard
for row in chessboard:
    print(' '.join(row))
