def DNA_strand(lol):
	new_string = []
	for i, char in enumerate(lol):
		if char == "A":
			new_string.append("T")
		elif char == "T":
			new_string.append("A")
		elif char == "G":
			new_string.append("C")
		elif char == "C":
			new_string.append("G")
	return "".join(new_string)


print(DNA_strand("ATTGC"))
