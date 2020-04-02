import numpy as np
import copy


def find_adjacent_neighbors(array, letter, start_index=None):
	"""
	Find vertical, horizontal and diagonal neighbors of a given element
	:param board_shape:
	:return:
	"""
	if start_index is None:
		indexes = np.argwhere(array == letter)
		if len(indexes) > 1:
			neighbors = []
			for i, j in indexes:
				n1 = array[i - 1][j - 1]
				n2 = array[i - 1][j]
				n3 = array[i - 1][j + 1]
				n4 = array[i][j - 1]
				n5 = array[i][j + 1]
				n6 = array[i + 1][j - 1]
				n7 = array[i + 1][j]
				n8 = array[i + 1][j + 1]
				neighbors.append([n1, n2, n3, n4, n5, n6, n7, n8])

	else:
		neighbors = {}
		i, j = start_index[0],  start_index[1]
		neighbors[array[i - 1][j - 1]] = [i - 1, j - 1]
		neighbors[array[i - 1][j]] = [i - 1, j]
		neighbors[array[i - 1][j + 1]] = [i - 1, j + 1]
		neighbors[array[i][j - 1]] = [i, j - 1]
		neighbors[array[i][j + 1]] = [i, j + 1]
		neighbors[array[i + 1][j - 1]] = [i + 1, j - 1]
		neighbors[array[i + 1][j]] = [i + 1, j]
		neighbors[array[i + 1][j + 1]] = [i + 1, j + 1]
	return neighbors


def find_word(board, word):
	print(board, word)
	board = np.array(board)
	board = np.pad(board, (1, 1), mode='constant')
	boards = []
	possible_starts = len(np.argwhere(board == word[0]))
	for i in range(possible_starts):
		boards.append(copy.deepcopy(board))

	if possible_starts > 0 and len(word) == 1:
		return True
	if possible_starts == 0:
		return False

	for idx, letter in enumerate(word[:-1]):
		start_index = np.argwhere(boards[i] == word[0])[i]
		board = boards[i]
		



		for idx, letter in enumerate(word[:-1]):

			# Find neighbors
			neighbors = find_adjacent_neighbors(board, letter, start_index)

			# Check if next letter is a neighbor
			next_letter = word[idx + 1]
			if next_letter in neighbors.keys():
				new_ways = np.argwhere(np.array(neighbors.keys()))
				if len(np.argwhere(np.array(neighbors.keys()))) > 1:
					print("hold")
				board[start_index[0]][start_index[1]] = ""
				start_index = neighbors[next_letter]
				if idx + 2 == len(word):
					return True
				continue
			else:
				break
	return False


def find_word(board, word):
	print(board, word)
	board = np.array(board)
	board = np.pad(board, (1, 1), mode='constant')
	boards = []
	possible_starts = len(np.argwhere(board == word[0]))
	for i in range(possible_starts):
		boards.append(copy.deepcopy(board))

	if possible_starts > 0 and len(word) == 1:
		return True
	if possible_starts == 0:
		return False

	for i in range(possible_starts):
		start_index = np.argwhere(boards[i] == word[0])[i]
		board = boards[i]
		for idx, letter in enumerate(word[:-1]):

			# Find neighbors
			neighbors = find_adjacent_neighbors(board, letter, start_index)

			# Check if next letter is a neighbor
			next_letter = word[idx + 1]
			if next_letter in neighbors.keys():
				new_ways = np.argwhere(np.array(neighbors.keys()))
				if len(np.argwhere(np.array(neighbors.keys()))) > 1:
					print("hold")
				board[start_index[0]][start_index[1]] = ""
				start_index = neighbors[next_letter]
				if idx + 2 == len(word):
					return True
				continue
			else:
				break
	return False




testBoard = [['T', 'T', 'M', 'D', 'X'],
			 ['G', 'Y', 'I', 'N', 'N'],
			 ['P', 'X', 'L', 'C', 'E'],
			 ['I', 'A', 'U', 'L', 'G'],
			 ['A', 'M', 'I', 'N', 'A']]

print(find_word(testBoard, "ANIMAL"), True, "Test for ANIMAL")
# print(find_word(testBoard, "EARS"), False, "Test for EARS")
# print(find_word(testBoard, "EAR"), True, "Test for EAR")
# print(find_word(testBoard, "C"), True, "Test for C")
# print(find_word(testBoard, "BAILER"), True, "Test for BAILER")
# print(find_word(testBoard, "RSCAREIOYBAILNEA"), True, "Test for RSCAREIOYBAILNEA")
# print(find_word(testBoard, "ROBES"), False, "Test for ROBES")