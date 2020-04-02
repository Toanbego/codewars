from itertools import combinations
import numpy as np
def choose_best_sum(t, k, ls):
	"""

	:param t: max distance
	:param k: number of towns
	:param ls: distances to each town
	:return:
	"""
	r = combinations(ls, k)
	distances = []
	for perm in r:
		distances.append(sum(perm))
	distance_array = np.unique(np.array(distances))
	try:
		return np.max(distance_array[(np.argwhere(distance_array <= t))])
	except ValueError:
		return None




xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(430, 8, xs))
