def xo(s):
	s = s.lower()
	exes = 0
	ohs = 0
	for c in s:
		if c == 'x':
			exes += 1
		elif c == 'o':
			ohs += 1
	if exes == ohs:
		return True
	else:
		return False

print(xo('xxxOooM'))


