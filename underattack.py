import numpy as np
#5x5 mini-chess board, create a 2D NumPy array
#black knights = int 1, white pawn = 2, empty spaces = 0.
arr = np.zeros((5, 5))

for i, row in enumerate(arr):
    for j, element in enumerate(row):
        if i == 0 or i == 4 or j == 0 or j == 4:
            arr[i][j] = 1
        if i == 2 and j == 2:
            arr[i][j] = 2
print(arr)

#part b: function takes in board, returns list of knights that threaten the pawn
def underAttack(arr):
    tester = [] #list for knight indices
    #possible knight moves
    X=[-1, 1, 2, 2, 1, -1, -2, -2]
    Y=[2, 2, 1, -1, -2, -2, -1, 1]

    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            for ctr in range(8):
                xAxis = i + X[ctr]
                yAxis = j + Y[ctr]
                #if this is in fucking bounds , else do nothing
                if xAxis > 0 and xAxis < 5 and yAxis > 0 and yAxis < 5:
                    if arr[xAxis, yAxis] == 2: #check for pawn
                        tester.append([i, j])
    print(tester)

underAttack(arr)
