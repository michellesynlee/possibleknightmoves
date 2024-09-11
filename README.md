# possibleknightmoves
Data structures/matrices practice

a. Consider the following 5x5 mini-chess board. Assuming that the top left corner is (0, 0) and any cell in the board is represented with (i, j) where i is the row and j is column, create a 2D NumPy array where black knights are represented with integer 1, white pawn is represented with 2, and empty spaces are represented with 0. Return this array in the associated function.

b. Now suppose you are controlling the white pawn. Write a Python function that takes in any such board configu-
ration x (i.e. a NumPy array) as the only argument and returns a list of indices of the black knights that currently threaten the white pawn (e.g. [(0, 1), (0, 3), ...]). This should work for all cases (i.e. any 5x5 board with black knights as 1s and a single white pawn as 2).
