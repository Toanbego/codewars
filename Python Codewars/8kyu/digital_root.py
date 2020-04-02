def digital_root(n):
	while len(str(n)) > 1:
		n = sum([int(digit) for digit in str(n)])
	return n


print(digital_root(456))
