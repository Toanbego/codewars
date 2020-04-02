import numpy as np


def same_structure_as(original, other):
	"""
	:param original:
	:param other:
	:return:
	"""
	if isinstance(original, list) and isinstance(other, list):
		nest_struct1 = []
		nest_struct2 = []

		for elem in original:
			nest_struct1.append(np.array(elem).shape)

		for elem in other:
			nest_struct2.append(np.array(elem).shape)

		if nest_struct1 == nest_struct2:
			return True
		else:
			return False
	else:
		return False



print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
print(same_structure_as([], {}))
print(same_structure_as([], 1))

