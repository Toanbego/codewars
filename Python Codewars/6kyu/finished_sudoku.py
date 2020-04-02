
import numpy as np


def done_or_not(sudoku):
	sudoku_arr = np.array(sudoku)
	regions = np.reshape(sudoku_arr, (27, 3))
	idx1 = 0
	valid_length = 9
	for row, column in zip(sudoku_arr, sudoku_arr.transpose()):
		region = np.ravel(np.array((regions[idx1], regions[idx1 + 3], regions[idx1 + 6])))
		if len(np.unique(row)) != valid_length or \
				len(np.unique(column)) != valid_length or \
				len(np.unique(region)) != valid_length:
			return False
	return True


valid = done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
		   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
		   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
		   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
		   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
		   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
		   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
		   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
		   , [8, 7, 9, 6, 4, 2, 1, 5, 3]])
print(valid)
valid = done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
		   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
		   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
		   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
		   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
		   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
		   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
		   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
		   , [8, 7, 9, 6, 4, 2, 1, 3, 5]])
print(valid)