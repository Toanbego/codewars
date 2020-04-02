import numpy as np
import copy

def get_char_position(string, triplet):
	pos1 = np.argwhere(string == triplet[0])[0][0]
	pos2 = np.argwhere(string == triplet[1])[0][0]
	pos3 = np.argwhere(string == triplet[2])[0][0]
	return pos1, pos2, pos3

def recoverSecret(triplets):
	"""
	Triplets is a list of triplets from the secrent string. Return the string.
	:param triplets:
	:return:
	"""
	string = np.unique(np.array(triplets))

	is_moving = True
	while is_moving:
		old_string = copy.deepcopy(string)
		for triplet in triplets:
			tmp1, tmp2, tmp3 = get_char_position(string, triplet)
			if tmp1 > tmp2:
				string[tmp1], string[tmp2] = triplet[1], triplet[0]
				tmp1, tmp2, tmp3 = get_char_position(string, triplet)
			if tmp1 > tmp3:
				string[tmp1], string[tmp3] = triplet[2], triplet[0]
				tmp1, tmp2, tmp3 = get_char_position(string, triplet)
			if tmp2 > tmp3:
				string[tmp2], string[tmp3] = triplet[2], triplet[1]

		if np.array_equal(old_string, string):
			break
	return "".join(string)




secret = "whatisup"
triplets = [
			['t', 'u', 'p'],
			['w', 'h', 'i'],
			['t', 's', 'u'],
			['a', 't', 's'],
			['h', 'a', 'p'],
			['t', 'i', 's'],
			['w', 'h', 's']]
print(recoverSecret(triplets))
